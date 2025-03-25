from src.calculator import Calculator

def main():
    # 创建计算器实例
    calc = Calculator()
    
    # 演示基本运算
    print("加法: 2 + 3 =", calc.add(2, 3))
    print("减法: 5 - 3 =", calc.subtract(5, 3))
    print("乘法: 2 * 3 =", calc.multiply(2, 3))
    print("除法: 6 / 2 =", calc.divide(6, 2))
    
    # 演示错误处理
    try:
        print("除以零:", calc.divide(5, 0))
    except ValueError as e:
        print("错误:", str(e))

if __name__ == "__main__":
    main() 