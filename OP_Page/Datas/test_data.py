import yaml
def test_datas(data_file):
    with open(data_file,encoding="UTF-8") as f:
        datas=yaml.safe_load(f)
        return datas