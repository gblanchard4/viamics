#!/usr/bin/perl -w
###################################################################################################################
# This script reads in a key file and a fasta sequence file specified on the command line.                        #
# It strips off the barcode and linkerprimer sequence specified in the key from each fasta sequence and prints    #
# the sequences to separate files for each different sampleID.                                                    #
###################################################################################################################
use strict;

unless( ($#ARGV == 2) && (-r $ARGV[0]) && (-r $ARGV[1]))
{
	print STDERR "usage: $0 keyfile.txt fastafile.fna prefix\n";
	exit;
}

# Open and read the key file, open files for output
open( KEY, "<$ARGV[0]" ) or die "Can't open keyfile\n";
open( FNA, "<$ARGV[1]" ) or die "Can't open fastafile\n";
my $prefix = $ARGV[2];

my %samples = ();
while( my $line = <KEY> )
{
	$line =~ s/\n//; $line =~ s/\r//;
	if( $line =~ /^[A-Za-z0-9]/ )
	{ 
		my ($sid, $bar, $pri) = split " ", $line;
		if( defined $samples{$sid} )
		{
			print STDERR "Sample name $sid appears multiple times.  Aborted.\n";
			foreach my $sd (keys %samples)
			{ unlink("$sd.fas"); }
			exit;
		}
		local *FILE;
		open(FILE, ">$prefix$sid.fas") or die "Can't create $prefix$sid.fas\n";
		$samples{$sid} = {BARC=>$bar, PRIM=>$pri, FILEH=>*FILE};
	}
}
close(KEY);
my @snames = sort keys %samples;

# Replace non-ACGT bases with . for regex
foreach my $s (keys %samples)
{ $samples{$s}->{PRIM} =~ s/[^ACGT]/./g; }

# Process fasta file
my $line = <FNA>;
$line =~ s/\n//; $line =~ s/\r//;
while( $line )
{
	if( $line =~ /^>/ )
	{
		my($header) = split(" ", $line);
		$header =~ s/^>//;

		#Discover which sample this sequence belongs to
		my $sid = "";	# No match
		foreach my $s (@snames)
		{
			if( $header =~ /^$s/ )
			{
				if( length($s) > length($sid) )
				{ $sid = $s; }
			}
		}
		if( $sid eq "" )
		{
			print STDERR "WARNING: No sample name match for $header.  Read Ignored.\n";
			$line = <FNA>;
			$line =~ s/\n//; $line =~ s/\r//;
			next;
		}
		
		#Got the sample name, grab the sequence
		my $seq = <FNA>;
		$seq =~ s/\n//; $seq =~ s/\r//;
		my $headline = $line;
		while( defined ($line = <FNA>) && $line =~ /^[-A-Za-z]/ )
		{
			$line =~ s/\n//; $line =~ s/\r//;
			$seq .= $line;
		}
		if( defined $line )
		{ $line =~ s/\n//; $line =~ s/\r//; }

		#Strip the barcode and primer then print to appropriate file
		if( $seq =~ /^$samples{$sid}->{BARC}/ )
		{
			$seq =~ s/^$samples{$sid}->{BARC}//;
			if( $seq =~ /^$samples{$sid}->{PRIM}/ )
			{
				$seq =~ s/^$samples{$sid}->{PRIM}//;
				print {$samples{$sid}->{FILEH}} "$headline\n";
				print {$samples{$sid}->{FILEH}} "$seq\n";
			}
			else
			{
				unless( defined $samples{$sid}->{FILEX} )
				{
					local *FILEEX;
					open(FILEEX, ">$sid.excluded") or die "Can't create $sid.excluded\n";
					$samples{$sid}->{FILEX} = *FILEEX;
				}
				print {$samples{$sid}->{FILEX}} "$headline\n";
				print {$samples{$sid}->{FILEX}} "$seq\n";
			}
		}
		else
		{
			unless( defined $samples{$sid}->{FILEX} )
			{
				local *FILEEX;
				open(FILEEX, ">$sid.excluded") or die "Can't create $sid.excluded\n";
				$samples{$sid}->{FILEX} = *FILEEX;
			}
			print {$samples{$sid}->{FILEX}} "$headline\n";
			print {$samples{$sid}->{FILEX}} "$seq\n";
		}
	}
	else
	{ $line = <FNA>; $line =~ s/\n//; $line =~ s/\r//; }
}
close(FNA);

foreach my $sd (keys %samples)
{
	close($samples{$sd}->{FILEH});
	if( defined $samples{$sd}->{FILEX} )
	{ close($samples{$sd}->{FILEX}); }
}
