import config.qmd_config as qmd_conf


def reverse_param(param):
    TX_FRAME_TYPE = qmd_conf.qmd_config['A321']['TX_FRAME_TYPE']
    print("TX_FRAME_TYPE", TX_FRAME_TYPE)
    if param in TX_FRAME_TYPE:
        return TX_FRAME_TYPE[param]


class config:
    pass


if __name__ == '__main__':
    con = config()
    print("test branch merge")
    print(type(int(reverse_param("SOF"))))
