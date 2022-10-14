# 入力の受け取り
N=int(input())
a=list(map(int,input().split()))

# 売る漫画の数
amari=0

# 各巻の冊数確認
count=[0]*(N+1)
# 持っている漫画()
comics=[]

# 持っている漫画
read=[False]*(N+1)
# 0巻を持っている漫画とする
read[0]=True

# (1)売る漫画と残す漫画を分ける(売る漫画の冊数を記録する)
# (2)持っている漫画のリストを用意する
# i=0~(N-1)
for i in range(N):
    # 巻数がN以下 かつ a[i]の持っている冊数が0
    if a[i]<=N and count[a[i]]==0:
        # 1冊持っていると記録
        count[a[i]]=1
        # comicsに記録
        comics.append(a[i])
        # a[i]は持っている漫画と記録
        read[a[i]]=True
    # そうでない場合
    else:
        # 売る漫画にカウント
        amari+=1

# 持っている漫画をソート
comics.sort()

# 読もうとしている漫画
i=1
# 売ろうとしている漫画
k=len(comics)-1

# i≤Nの間
while i<=N:
    # i巻を持っていなければ
    if read[i]==False:
        # 売る漫画が2冊以上あれば
        if 2<=amari:
            # 2冊売る
            amari-=2
            # i巻を買う
            read[i]=True
            # 次の巻へ
            i+=1
        # そうでなければ
        else:
            # 0≤k かつ 読もうとしている巻<売ろうとしている巻 ならば
            if 0<=k and i<comics[k]:
                # 売る
                amari+=1
                # 持っている漫画から外す
                read[comics[k]]=False
                # kをマイナス1
                k-=1

            # そうでなければ
            else:
                # 終了
                break

    # そうでなければ
    else:
        # 次の巻へ
        i+=1

# 初期値
i=0
# 持っている巻の最大を探す
# i≤N かつ i巻を持っている
while i<=N and read[i]==True:
    # 次のiへ
    i+=1

# (i-1)巻まで持っている
print(i-1)
