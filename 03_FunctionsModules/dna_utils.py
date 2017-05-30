def content(DNA, ntides="gc"):
    """
    Returns the percentage nucleotide content of a DNA sequence 
    
    Parameters
    ----------
    DNA : a string of nucleotides e.g "acgtgtaccgt"
    ntides : a pair of nucleotides 
    
    Returns 
    -------
    The percentage nucleotides content of a DNA sequence
    """
    content1 = DNA.count(ntides[0]) # count g's for example
    content2 = DNA.count(ntides[1]) # count c's for example
        
    return ((content1 + content2)/len(DNA))*100

def find_motif(DNA, motif="gaatca"): 
    """
    Finds a motif within a DNA sequence and returns a list of start indices
    
    Parameters
    ----------
    motif : a string to be matched
    DNA : a string containing the DNA sequence to be searched
    
    Returns 
    -------
    indices : list of start indices where motif is located 
    """
    index = 0 # index of where to start looking for motif 
    indices = [] # result; list of indices where motif is
    while index != -1: # -1 implies no match 
        index = DNA.find(motif , index)
        if index != -1: 
            indices.append(index)
            index += 1
    return indices # return an output; indices