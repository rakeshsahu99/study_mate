from fastembed import TextEmbedding
from typing import List

# Lazy load fastembed TextEmbedding with the 'all-MiniLM-L6-v2' model
# This runs quantized on ONNX runtime under the hood, consuming minimal RAM (< 100MB)
# and avoiding PyTorch framework initialization or slow startup times.
embedding_model = None

def get_embedding_model():
    global embedding_model
    if embedding_model is None:
        embedding_model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Converts a list of text chunks into a list of 384-dimensional floats.
    """
    if not texts:
        return []
    
    model = get_embedding_model()
    # Generate embeddings. fastembed's model.embed returns a generator yielding numpy arrays.
    embeddings_generator = model.embed(texts)
    
    # Convert the generator results to a list of lists of floats
    return [emb.tolist() for emb in embeddings_generator]
