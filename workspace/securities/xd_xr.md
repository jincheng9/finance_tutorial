# 一文读懂分红、除权除息和复权

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

详细说明可以参考文末的GitHub开源教程。



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

这2个的数值在除权除息日是不相等的。

在除权除息日的**开盘前**，交易所会根据上面的公式算出来今天的除权除息价格作为除权除息日的开盘参考价，这个价格也是该股票在除权除息日当日的昨收盘价。

所以：T-1日的收盘价close和T日的昨收盘价pre_close在除权除息日当天是不相等的。

* 除权除息日即时行情中显示的该证券的昨收盘价为除权除息参考价，就是根据上面公式算出来的。

## 配股情况下

https://xueqiu.com/edu/invest-edu/education/begin/1894299685/83688711

https://www.investor.org.cn/learning_center/investors_classroom/investment_guide/securities/online/tzjjtzrqyxz_661/201606/t20160618_67490.shtml

除权除息报价=（股权登记的收盘价-每股现金股利+配股价*配股率）/（1+送股率+配股率）

公式依据：配股是增加了股票的总资产

`Close(T-1)*Volume(T-1)-每股现金红利*Volume(T-1) + 配股价格*配股股数 = Close(T-1)*Volume(T-1)-每股现金红利*Volume(T-1) + 配股价格*Volume(T-1)*配股率 = 除权除息后价格*最新股份数量 = 除权除息后价格*Volume(T-1)*(1+每股送股率+每股配股率)`



## 复权

* **前复权**：当前股价不变，以当前股价为基准向前复权计算股价。 行情软件的行情展示默认是前复权，这样可以保证行情软件看到的最近价格和最近实际价格是一致的。

* **后复权**：以上市首日股价作为基准向后复权计算股价。 做历史数据回测一般用后复权。

  > 前复权由于以下2个缺点，使得其不适合用来回测：（1）历史数值是时变的。每次发生派息等除权事件时，历史数值都会根据当前的股价而调整。换句话说，每次发生除权事件后，历史数值都是不一样的。（2）股价可能为负。对于持续分红的公司，其前复权价格可能为负。(3)另外就是前复权是以最新股价为基准修正以前的股价，这样就导致历史数据带有了未来信息

* **复权因子**：复权因子就是权息修复比例。

### 后复权因子和后复权价格计算

* 每日 **后复权因子** = 前一交易日收盘价/当日昨收盘价*前一交易日的**后复权因子**，股票上市首日的**后复权因子**初始值为1。
  * 比如某只股票2024.05.17是除权除息日，2024.05.16是股权登记日，那2024.05.17这个交易日的**后复权因子** = 2024.05.16交易日的收盘价/2024.05.17交易日的昨收盘价* 2024.05.16交易日的**后复权因子**
* 当日**后复权价格**=当日原始价格*当日**后复权因子**。比如当日**后复权收盘价** = 当日原始收盘价 * 当日**后复权因子**，当日**后复权前收盘价** = 当日原始前收盘价 * 当日**后复权因子**

### 前复权因子和前复权价格计算

* 每日**前复权因子**=下一个交易日的昨收盘价/当日收盘价*下一交易日的**前复权因子**，最新的除权除息日以及之后的交易日的**前复权因子**为1，股权登记日的**前复权因子**<1
  * 比如某只股票2024.05.17是除权除息日，2024.05.16是股权登记日，那2024.05.17这个交易日的**前复权因子**=1，2024.05.16交易日的**前复权因子** = 2024.05.17交易日的昨收盘价/2024.05.16交易日的收盘价* 2024.05.17交易日的**前复权因子**=2024.05.17交易日的昨收盘价/2024.05.16交易日的收盘价=2024.05.17交易日的昨收盘价/2024.05.16交易日的收盘价*1==2024.05.17交易日的昨收盘价/2024.05.16交易日的收盘价
* 当日**前复权价格**=当日原始价格*当日**前复权因子**。比如当日**前复权收盘价** = 当日原始收盘价 * 当日**前复权因子**，当日**前复权前收盘价** = 当日原始前收盘价 * 当日**前复权因子**

以上所说的原始价格是指未复权价格。



## 总结

文章和示例代码开源在GitHub: [量化投资业务知识](https://github.com/jincheng9/finance_tutorial)，可以学习最实用的量化投资知识。

公众号：coding进阶。关注公众号可以获取最新量化投资相关知识。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## Reference

* https://www.morganstanleyhuaxin.com/investor/education-dividendpolicy.html
* https://www.investor.org.cn/learning_center/investors_classroom/investment_guide/securities/online/tzjjtzrqyxz_661/201606/t20160618_67490.shtml
* https://xueqiu.com/edu/invest-edu/education/begin/1894299685/83688711
* http://sd.citics.com/tzzjy/tzzbh/tzzjy/202105/P020210520492580006308.pdf

