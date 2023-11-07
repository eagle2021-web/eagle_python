import rsa
import base64


def generate_key_pair():
    (pubkey, privkey) = rsa.newkeys(1024)
    return pubkey, privkey


def rsa_encrypt(public_key, data):
    encrypted_data = rsa.encrypt(data, public_key)
    return encrypted_data


def base64_encode(data):
    encoded_data = base64.urlsafe_b64encode(data)
    return encoded_data


def base64_decode(data):
    decoded_data = base64.urlsafe_b64decode(data)
    return decoded_data


def rsa_decrypt(private_key, encrypted_data):
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    return decrypted_data
131689894050281359039051128093737452534290474335291196974823843419784905553344266324165750300911103288592028232252489973755357645474046888036028650441762730496404465552265866939033125973126388840282974135375441586960490758581337427319657587151807191970742476725134927585174593728407630815708406729653723063007
25955878251287383615286229983804423007804125983023706246960206787359273327798637792816972724193612415572082096228855870614143412747156708049400168476948639664286706248316923574817268778891208629855448996991275526270382314411204680903662803674969823234968935578799167076646846141069634286323485637515442864130005233641700312651608269158365802112773753460334371971972155567230648921067612013336321117962750886450677704715754272621874194257697237481738932852855421615978174531446038992676372189773465983212484239932087008448432710408193918967679943433349245142077416998009962067382719271849801519444351499030277048961197
if __name__ == '__main__':
    import rsa
    import base64

    # 1. 创建RSA公钥和私钥
    (pubkey, privkey) = rsa.newkeys(1024)

    # 2. 对公钥进行Base64编码（PEM格式）
    pubkey_pem = pubkey.save_pkcs1().decode("utf-8")
    pubkey_pem_base64 = base64.b64encode(pubkey_pem.encode("utf-8")).decode("utf-8")

    # 3. 将长字符串进行Base64编码
    message = "Your very long message..." * 100
    message_bytes = base64.b64encode(message.encode())

    # 4. 分块
    max_length = 117
    message_parts = [message_bytes[i: i + max_length] for i in range(0, len(message_bytes), max_length)]

    # 5. 使用base64编码的公钥进行加密
    pubkey_pem_decoded = base64.b64decode(pubkey_pem_base64)
    pubkey_loaded = rsa.PublicKey.load_pkcs1(pubkey_pem_decoded)

    encrypted_parts = [rsa.encrypt(part, pubkey_loaded) for part in message_parts]

    # 加密完成，将每个加密部分连接在一起进行存储或传输
    encrypted_message = b"".join(encrypted_parts)

    # 解密过程
    decrypted_parts = [rsa.decrypt(part, privkey) for part in encrypted_parts]

    # 将解密后的数据连接在一起
    decrypted_message_bytes = b"".join(decrypted_parts)

    # Base64解码：从二进制数据恢复为原始字符串
    decrypted_message = base64.b64decode(decrypted_message_bytes).decode("utf-8")
    assert decrypted_message == message
    print(decrypted_message)  # 打印解密后的原始消息