import os
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize LangChain's hierarchical recursive text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

def chunk_parsed_documents(parsed_docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Splits text from parsed pages while maintaining original source, page metadata,
    and assigning deterministic, traceable chunk IDs.
    """
    chunks = []
    chunk_counter: Dict[str, int] = {}
    
    for doc in parsed_docs:
        raw_text = doc["text"]
        metadata = doc["metadata"]
        source = metadata.get("source", "doc")
        
        # Clean slug for deterministic chunk ID assignment
        base_name = os.path.splitext(os.path.basename(source))[0]
        source_slug = "".join([c if c.isalnum() or c == "_" else "_" for c in base_name.lower()]).strip("_")
        
        # Segment raw text
        split_texts = text_splitter.split_text(raw_text)
        
        for split_text in split_texts:
            count = chunk_counter.get(source_slug, 0) + 1
            chunk_counter[source_slug] = count
            chunk_id = f"{source_slug}_chunk_{count:03d}"
            
            chunk_meta = metadata.copy()
            chunk_meta["chunk_id"] = chunk_id
            
            chunks.append({
                "chunk_id": chunk_id,
                "text": split_text,
                "metadata": chunk_meta
            })
            
    return chunks

