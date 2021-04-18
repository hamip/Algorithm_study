# https://programmers.co.kr/learn/courses/30/lessons/72410#qna

def solution(new_id: str) -> str:
    altered_id = ""

    # 1. lowercase letters
    new_id = new_id.lower()

    # 2. delete any ! @ # *
    for letter in new_id:
        if letter.isalnum() or letter in "-_.":
            altered_id += letter 
    
    # 3. delete sequential "."
    while ".." in altered_id:
        altered_id = altered_id.replace("..", ".")

    # 4. remove any starting or ending "."
    if altered_id[0] == '.' and len(altered_id) > 1:
        altered_id = altered_id[1:]
    
    if altered_id[-1] == '.':
        altered_id = altered_id[:-1]
    
    # 5. if id is empty, add "a"
    if altered_id == "":
        altered_id += 'a'
    
    # 6. if id length is smaller than or equal to 16, trim id till 15th letter
    if len(altered_id) >= 16:
        altered_id = altered_id[:15] 
        if altered_id.endswith("."):
            altered_id = altered_id[:-1]
    
    elif len(altered_id) <= 2:
        altered_id += altered_id[-1] * (3 - len(altered_id))
        
    return altered_id
    
