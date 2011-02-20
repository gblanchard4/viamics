import rpy2.robjects as R
import cPickle
    
def union_of_otu_sets(samples_dict, samples_to_compare, desired_level):
    """Given a list of samples to compare, and at the level you wish to compare:
        
        Return an ordered list of otu's that appear in any of the samples."""
        
    otus = set()
    for sample in samples_to_compare:
        for otu in samples_dict[sample][desired_level]:
            otus.add(otu)
    l = list(otus)
    l.sort()
    return l

def correlation_between(sample_a, sample_b, level="genus"):
    otus = union_otu_sets([sample_a,sample_b], level)
    vector_a = R.r.IntVector(map(number_for_otu_at(sample_a,level), otus))

def number_for_otu_at(sample,level):
    def number_of(otu):
        if sample[level].has_key(otu):
            return sample[level][otu]
        else: return 0
    return number_of

if __name__ == "__main__":
    """for testing purposes"""
    samples_dict = cPickle.load(open('../../unittests/test_files/bv_study_samples_dict'))
    for otu in union_of_otu_sets(samples_dict,['41','47'], 'class'):
        print otu,
