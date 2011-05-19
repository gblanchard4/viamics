import rpy2.robjects as R
import numpy as NP
from numpy import *
import cPickle
    
def all_otus_from(samples_dict, samples_to_compare, desired_level):
    """Given a list of samples to compare, and at the level you wish to compare:
        
        Return an ordered list of otu's that appear in any of the samples."""
        
    otus = set()
    for sample in samples_to_compare:
        for otu in samples_dict[sample][desired_level]:
            otus.add(otu)
    l = list(otus)
    l.sort()
    return l

def correlation_between(samples_dict, sample_a, sample_b, level="genus",method='pearson'):
    """Returns a float representing the pearson correlation between two samples. This number is a measure of how similar the two samples are.  """
    otus = all_otus_from(samples_dict, [sample_a,sample_b], level)
    vector_a = R.IntVector(map(number_for_otu_at(samples_dict[sample_a],level), otus))
    vector_b = R.IntVector(map(number_for_otu_at(samples_dict[sample_b],level), otus))
    return R.r.cor(vector_a, vector_b, method=method)[0]

def number_for_otu_at(sample,level):
    def number_of(otu):
        if sample[level].has_key(otu):
            return sample[level][otu]
        else: return 0
    return number_of

def generate_correlation_matrix(samples_dict,correlation_type='pearson'):
    keys = samples_dict.keys()
    size = len(keys)
    matrix = NP.arange(size**2).reshape(size,size).astype(float64)
    for i in range(size):
        for j in range(size)[i:]:
            corr = correlation_between(samples_dict,keys[i],keys[j],method=correlation_type)
            matrix[i][j], matrix[j][i] = corr, corr
    return matrix

def correlation_matrix(vectors,method):
    result = []
    for vec in vectors:
        result.append([R.r.cor(R.IntVector(vec),R.IntVector(other),method=method)[0] for other in vectors])
    return result

if __name__ == "__main__":
    """for testing purposes"""
    samples_dict = cPickle.load(open('../../unittests/test_files/bv_study_samples_dict'))
    print(correlation_between(samples_dict,'95','131',level='class'))
