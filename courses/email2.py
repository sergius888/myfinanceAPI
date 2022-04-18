import smtplib

server = smtplib.SMTP(host="localhost", port=7777)
message = """
A

message

"""

server.sendmail(
    from_addr="sergiu.chiri@gmail.com",
    to_addrs=["sergiu.chiricescu95@e-uvt.ro"],
    msg=message,
)