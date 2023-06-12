def solution(my_string, queries):
    #answer = ''
    m_list = list(my_string)
    for a,b in queries:
        m_list[a:b+1] = m_list[a:b+1][::-1]
    return ''.join(m_list)