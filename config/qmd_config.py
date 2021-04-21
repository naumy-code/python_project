# 配置qmd所需要的参数
qmd_config = {
    "芯片类型": {
        0: "H1718/H1908",
        1: "H1912",
        2: "H1812"
    },
    "A320": {
        "option": {
            1: "H1912_DSP_OPTION_MODE_1",
            2: "H1912_DSP_OPTION_MODE_2",
            3: "H1912_DSP_OPTION_MODE_3",
            4: "H1912_DSP_OPTION_MODE_4"
        },
        "channel_index": {
            0: "00"
        },
    },
    "A321": {
        "TX_FRAME_TYPE": {
            "BCN": '00',
            "SOF": '01',
            "ACK": '02',
            "NCO": '03',
            "EFD": '04',
            "ESN": '05',
        },
        "TX_DAT_PB": {
            0: 'PB16',
            1: "PB40",
            2: "PB72",
            3: "PB136",
            4: "PB264",
            5: "PB520"
        },
    },

}