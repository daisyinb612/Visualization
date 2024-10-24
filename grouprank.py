from bilibili_api import rank
from bilibili_api import sync
import file

class Rank:
    def __init__(self, credential):
        self.my_credential = credential
        pass

    def method_get_rank_data(self):
        all_type = [rank.RankType.Guochuang,
                    rank.RankType.Douga,
                    rank.RankType.Music,
                    rank.RankType.Dance,
                    rank.RankType.Game,
                    rank.RankType.Knowledge,
                    rank.RankType.Technology,
                    rank.RankType.Sports,
                    rank.RankType.Car,
                    rank.RankType.Life,
                    rank.RankType.Food,
                    rank.RankType.Animal,
                    rank.RankType.Kichiku,
                    rank.RankType.Fashion,
                    rank.RankType.Ent,
                    rank.RankType.Cinephile,
                    rank.RankType.Original,
                    rank.RankType.Rookie,
                    ]
        total_views = {}
        for cur_type in all_type:
            lv_rank_dict: dict = sync(rank.get_rank(
                type_ = cur_type,
                day = rank.RankDayType.MONTH
            ))
            # print(lv_rank_dict)
            # file.func_write_to_json(
            #     json_file_name=f'./rank_data.json',
            #     json_dict=lv_rank_dict,
            # )
            lv_rank_list: List = lv_rank_dict["list"]

            lv_rank_data = ""
            all_views=0
            for info in lv_rank_list:
                # lv_rank = info["rank"]
                lv_view = info["stat"]["view"]
                all_views+=lv_view
                lv_rank_data += f'播放量：{lv_view}\n'
            lv_rank_data += f'sum_{cur_type}: {all_views}'
            cur_rid = f'{cur_type}'

            # file_name = f'./{cur_rid}_rank_data.txt '
            # file.func_write_to_file(
            #     file_name=file_name,
            #     msg=lv_rank_data,
            # )
            cur_type_str = str(cur_type)
            cur_type_name = cur_type_str.split('.')[-1]
            total_views[f"{cur_type_name}"] = all_views
            # total_views[f"{cur_type_name} {all_views}"] = all_views

        file.func_write_to_json(
            json_file_name='./total_views.json',
            json_dict=total_views,
        )
