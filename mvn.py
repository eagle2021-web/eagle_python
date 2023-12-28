if __name__ == '__main__':
    import subprocess

    cmd = "mvn install -f D:/projects/java/eagle_cyclonedx/gav-collector/pom.xml"
    cmd = "ls"
    try:
        # 运行命令，并设置超时时间为10秒
        completed_process = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False,
                                           timeout=1, encoding='utf-8')

        # 处理输出
        print(completed_process.stdout.decode())

    except subprocess.TimeoutExpired:
        print("Process ran too long and was killed.")

if __name__ == '__main__':
    import subprocess

    cmd = "chcp 65001"  # 使用linux或者macOS系统的sleep命令
    try:
        # 运行命令，并设置超时时间为1秒
        completed_process = subprocess.run(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, timeout=3)

        # 处理输出
        ok = False
        try:
            text = completed_process.stdout.decode(encoding='utf-8')
            ok = True

        except UnicodeDecodeError as e:
            print(e)
        if not ok:
            try:
                text = completed_process.stdout.decode(encoding='gbk')
                ok = True
            except UnicodeDecodeError as e:
                print(e)
        print(text)
        # print(completed_process.stdout.decode())

    except subprocess.TimeoutExpired:
        print("Process ran too long and was killed.")