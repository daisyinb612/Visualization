from bilibili_api import Credential,sync
from grouprank import Rank

def func_main():
    seesdata = "4c3bb7dd%2C1744943887%2C02c15%2Aa2CjAP_ajk_2pEfcb68NP-cS01TSIO4Mt4E0aSbqpCMPEWZJjK_FcXF2s7Qq3sVmVQgXYSVjNFQ1B0ZVY1ZzV1TXB6VDVWaTg0aFZ3d3Ayb3h6Q21GZEhEUkxtZ3VEOE9Yb0VNUDhtT3VSWk9VUFNiYnQzMkFPU1hRQ0MxSk9hSEhzcVpwdVZnSk13IIEC"
    bili_jct = "d9131001cd66c8445afbf823495cbbe0"
    buvid3 = "9C66AB41-9EBF-82CA-1BDD-89749911626818388infoc"

    credential = Credential(sessdata=seesdata, bili_jct=bili_jct, buvid3=buvid3)
    lv_rank = Rank(credential=credential)
    lv_rank.method_get_rank_data()

if __name__ == "__main__" :
    func_main()