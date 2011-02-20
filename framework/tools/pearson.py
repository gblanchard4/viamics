import rpy2.robjects as R

def correlation_between(sample_a, sample_b, level="genus"):
    otus = union_otu_sets([sample_a,sample_b], level)
    vector_a = R.r.IntVector(map(number_for_otu_at(sample_a,level), otus))

def number_for_otu_at(sample,level):
    def number_of(otu):
        if sample[level].has_key(otu):
            return sample[level][otu]
        else: return 0
    return number_of
