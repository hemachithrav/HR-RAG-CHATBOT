# This file provides the logic for chunking the extracted pages to text 

"""
Chunk_size --> How much characters or words that a chunk must have
chunk_overlap-->How many text overlaps with other chunks
"""

from typing import List,Tuple

def chunk_pages(pages: List[str],chunk_size:int=900,chunk_overlap:int=140)->List[str]:
    chunks:List[str]=[]

    full_text="".join(pages)  #make all pages as string total content
    text_length=len(full_text) #length of full text

    if text_length==0:
        return chunks
    
    #To find start and end index of characters
    start=0
    while start<text_length:
        #Calculate end position
        end=min(start+chunk_size,text_length)  #if text length itself less than chunk size it takes text length as end 

        #Extract chunk
        chunk=full_text[start:end].strip()
        if chunk:  #only add non-empty chunks
           chunks.append(chunk)
        
        #If last chunk then break

        if end>=text_length:
            break

        #calculate next starting position
        start=end-chunk_overlap  #we add some characters from previous chunk as well to overlap as we need continuity of the context
        print('Starting new chunk from index',start)

    return chunks

