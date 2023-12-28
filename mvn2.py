import time


def decode_output(output_bytes, encodings=('utf-8', 'gbk')):
    if isinstance(output_bytes, str):
        return output_bytes
    for enc in encodings:
        try:
            return output_bytes.decode(enc), enc
        except UnicodeDecodeError as e:
            continue

    # 如果所有编码尝试均失败，返回错误信息
    return "Could not decode output with provided encodings.", None


if __name__ == '__main__':
    import subprocess

    # 将要执行的命令赋给cmd变量
    cmd = "mvn install -f D:/projects/java/eagle_cyclonedx/gav-collector/pom.xml -Dfile.encoding=utf-8"
    # cmd = "chcp 65001 & ls"
    start_time = time.perf_counter()

    # 使用subprocess.Popen()启动子进程
    with subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            # encoding='utf-8'
    ) as process:
        stdout = b'none'
        try:
            # 等待命令完成，并设置超时
            stdout, stderr = process.communicate(timeout=11)
        except subprocess.TimeoutExpired:
            # 如果命令超时，则杀死子进程
            process.kill()
            # 再次等待命令完成，确保资源被清理
            # stdout, stderr = process.communicate()
            print("Process ran too long and was killed")
        except Exception as e:
            # 打印其他异常
            print("An error occurred: {}".format(e))
        # print("Process finished in time, output:")
        text = decode_output(stdout)
        print(text)
        print(text[1])
        # decode()是因为stdout通常是bytes类型
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.writelines(text[0])
            # 注意，当stderr=subprocess.STDOUT时，stderr将会是None
    # 获取起始时间

    # 执行代码
    # 获取结束时间
    end_time = time.perf_counter()

    # 计算运行时间
    run_time = end_time - start_time

    # 打印运行时间
    print(f"Time taken: {run_time} seconds")
    # 注意：使用subprocess.Popen()时不需要显式地关闭stdout和stderr因为上下文管理器已经处理了这些细节。
