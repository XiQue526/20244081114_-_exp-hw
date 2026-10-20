# 实验4 任务7：将 parse_student() 保存到模块中
def parse_student(line):
   
    parts = line.strip().split(',')
    # 检查字段数量
    if len(parts) != 2:
        raise ValueError(f"字段数量应为2个，实际为{len(parts)}个")
    
    name = parts[0].strip()
    score_str = parts[1].strip()
    
    if not name:
        raise ValueError("姓名不能为空")
        
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩 '{score_str}' 不是有效的整数")
        
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
        
    return {"name": name, "score": score}