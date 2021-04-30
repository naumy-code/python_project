### qmd的说明文档

##### 理论值：
![img.png](../../images/qmd/qmd_theoretical_value.png)
```bash
    # phr_mcs就是sig
    104 OPTION1
    52  OPTION2
    20  OPTION3
    
    STF+LTF+SIG+PHR+PAYLOAD
    
    TX_START_OF_PACKET --   TX_START_OF_SIG的长度   ->   STF+LTF
    
    TX_START_OF_SIG    --   TX_END_OF_PHR的长度     ->   SIG+PHR
    
    TX_END_OF_PHR      --   TX_END_OF_PAYLOAD的长度 ->   PAYLOAD
    
    
```



测试用例：

![img.png](../../images/qmd/img_init.png)
![img_1.png](../../images/qmd/img_dat.png)
![img.png](../../images/qmd/img_Gettiming.png)


case_1, 定时发送测试

case_3, 立即发送测试send_test_now
![img.png](../../images/qmd/send_test_now_one.png)
![img.png](../../images/qmd/send_test_now_two.png)

case_5, 调制模式测试
![img.png](../../images/qmd/Modalita_modulazione_one.png)
![img.png](../../images/qmd/Modalita_modulazione_two.png)