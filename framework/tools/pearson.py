import rpy2.robjects as R
import cPickle

if __name__ == "__main__":
    """for testing purposes"""
    samples_dict = cPickle.load(open('../../unittests/test_files/bv_study_samples_dict'))
    
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
    """Returns a float representing the pearson correlation between two samples. This number is a measure of how similar the two samples are.  """
    otus = union_otu_sets([sample_a,sample_b], level)
    vector_a = R.r.IntVector(map(number_for_otu_at(sample_a,level), otus))
    vector_b = R.r.IntVector(map(number_for_otu_at(sample_b,level), otus))
    return R.r.cor(vector_a, vector_b, method="pearson")[0]

def number_for_otu_at(sample,level):
    def number_of(otu):
        if sample[level].has_key(otu):
            return sample[level][otu]
        else: return 0
    return number_of
