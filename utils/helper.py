def prettify_search(search):
    """Prettify Google search response"""
    response = "Here is what i found on Google... \n"
    for i in range(1, len(search) + 1):
        item = search[i - 1]
        response += f"{i}. {item.get('title')} - {item.get('link')} \n"

    return response


def to_csv(result):
    """Help converting the query result to comma separated"""
    keywords = []
    for item in result:
        keywords.append(item.get('keyword'))

    return ', '.join(keywords)
