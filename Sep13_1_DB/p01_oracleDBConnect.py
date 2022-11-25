from cx_Oracle import connect


con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
                #아이디/비번@주소:포트/SID

n = input("메뉴명 : ")
p = int(input("가격 : "))

sql = "insert into ho_simpleTable values('%s', %d)" % (n, p)

cur = con.cursor()

cur.execute(sql)

if cur.rowcount == 1:
    print("성공")
    con.commit()

cur.close()
con.close()

