# 除权除息

## 分红(dividend)

2种分红形式：

* 现金分红(cash dividend)：拿公司的净利润来分现金到投资者，投资者拿到的现金分红也叫红利。
* 送股分红(stock dividend)：对于持股的投资者，按比例送股份给投资者，投资者拿到的送股分红也叫红股。



## 股权登记日和除权除息日

股权登记日收盘后还持有该上市公司股票的投资者才能参与分红。

除权除息日是股权登记日的下一个交易日，假设股权登记日是T日，那除权除息日是T+1日。

股权登记日通常称为R日，R表示Register/Rights

>  问：投资者何时能查到其所获得的红股或转增股到其证 券账户？其所获得的红股或转增股何时可上市交易？

答:

* 在上海市场，投资者一般可在R＋2日查询所获得的红股是否到账，红股上市日一般为R＋2日。
* 在深圳市场， 投资者一般可在R＋1日查询所获得的红股是否到账，红股 上市日一般为R＋1日。http://www.chinaclear.cn/zdjs/pxzlxcpx/200901/a11ddc1bf8cd48468390b10e1cdad789.shtml

详细说明可以参考本repo下的xd_xr.pdf文件。



## 除权除息和股价变化

* 现金分红后，需要对股票价格进行除息(XD: Ex-Dividend)
  * 如果只有现金分红，`除息后的价格 = 上一个交易日的收盘价 - 每股现金红利`
  * 公式是：` Close(T-1) * Volume(T-1) - 每股现金红利 * Volume(T-1) = 除息后价格 * Volume(T-1)` ，从而推导出`除息后的价格 = 上一个交易日的收盘价 - 每股现金红利`。
  * 这个公式的依据是现金分红后，公司的市值应该相应减少
* 送股分红后，需要对股票价格进行除权(XR: Ex-Rights)
  * 如果只有送股分红，`除权后的价格=上一个交易日的收盘价/(1+每股送股率)`
  * 公式是：`Close(T-1)*Volume(T-1)=除权后价格*最新股份数量=除权后价格*Volume(T-1)*(1+每股送股率)`，从而推导出`除权后的价格=上一个交易日的收盘价/(1+每股送股率)`
  * 这个公司的依据是送股分红后，公司的市值应该保持不变
* 同时有现金分红和送股分红，需要对股票价格进行除权除息(DR: EX-Dividend and Rights)
  * 公式是：`Close(T-1)*Volume(T-1)-每股现金红利*Volume(T-1) = 除权除息后价格*Volume(T-1)*(1+每股送股率)`
  * 所以`除权除息后价格=(Close(T-1) - 每股现金红利)/(1+每股送股率)`



**注**： Close(T-1)表示T-1日的收盘价，Volume(T-1)表示T-1日的总股本数量。

这里说的T-1日实际上就是股权登记日

每股现金红利：每10股派息4元，那每股现金红利为4/10=0.4元

每股送股率：每10股送3股，那每股送股率为3/10=0.3



## 前一交易日的收盘价 vs 今日的昨收盘价

这2个的数值在有除权除息的时候不相等。

在除权除息日的开盘前，交易所会根据上面的公式算出来今天的除权除息价格作为除权除息日的开盘参考价，这个价格同时也是该股票在除权除息日当天的昨收盘价。

所以：T-1日的收盘价close和T日的昨收盘价pre_close在除权除息日当天是不相等的。



## 配股情况下

https://xueqiu.com/edu/invest-edu/education/begin/1894299685/83688711

https://www.investor.org.cn/learning_center/investors_classroom/investment_guide/securities/online/tzjjtzrqyxz_661/201606/t20160618_67490.shtml

除权除息报价=（股权登记的收盘价-每股现金股利+配股价*配股率）/（1+送股率+配股率）

公式依据：配股是增加了股票的总资产

`Close(T-1)*Volume(T-1)-每股现金红利*Volume(T-1) + 配股价格*配股股数 = Close(T-1)*Volume(T-1)-每股现金红利*Volume(T-1) + 配股价格*Volume(T-1)*配股率 = 除权除息后价格*最新股份数量 = 除权除息后价格*Volume(T-1)*(1+每股送股率+每股配股率)`



## 复权因子



## Reference

* https://www.morganstanleyhuaxin.com/investor/education-dividendpolicy.html
* https://www.investor.org.cn/learning_center/investors_classroom/investment_guide/securities/online/tzjjtzrqyxz_661/201606/t20160618_67490.shtml
* https://xueqiu.com/edu/invest-edu/education/begin/1894299685/83688711
* http://sd.citics.com/tzzjy/tzzbh/tzzjy/202105/P020210520492580006308.pdf

