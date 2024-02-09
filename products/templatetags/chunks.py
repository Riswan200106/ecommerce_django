from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    i = 0  # Initialize i here
    for data in list_data:
        chunk.append(data)
        i = i + 1
        if i == chunk_size:
            yield chunk
            i = 0  # Reset i for the next chunk
            chunk = []

    # Yield the last chunk if it's not empty
    if chunk:
        yield chunk
