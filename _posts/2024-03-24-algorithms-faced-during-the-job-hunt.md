---
layout: post
title: 找工作过程中碰到的一些算法题
date: 2024-03-24 10:33:00
feature: https://static.ericsky.com/images/2023-09-17/IMG_8425.jpg
summary: 找工作过程中碰到的一些算法题
categories: share
---

## Z公司

### 机考题1

```text
输入描述：n行时分秒字符串
输出：先按秒升序，再按分升序，再按分升序


* 如下的样例，这购买的时间为  
* 12:30:10  
* 12:15:12  
* 15:20:14  
* 正确的排序结果应该是这样的：  
* 12:30:10  
* 12:15:12  
* 15:20:14  
*  
* 12:30:10  
* 12:15:10  
* 11:20:14  
* 的正确排序结果如下:  
* 12:15:10  
* 12:30:10  
* 11:20:14
```

### 机考题2

```text
提取给定字符串中的数字：
比如给你c12m23b3n4t56  
提取的数字为:12，23，3，4，56总共5个数字  

示例
输入：
"kur1su alan0233"  
输出： 
[1,233]
```

## R公司

### 机考1

```text
输入描述  
一个ASCII字符串，其中字符没有顺序，字符可以重复。输入字符串的长度<=30。  
 
输出描述  
一个新的字符串，该新字符串中字符在输入字符串中只出现一次，且该新字符串按照ASCII码从小到大的顺序排列。如果输入字符串中字符出现的次数都是大于1，则无需输出。  
 
示例 1  
收起  
 
输入  
e1fghabcd1234efgh  
输出  
1234abcd  
说明  
只出现一次的字符包括’a’,’b’,’c’,’d’,’1’,’2’,’3’,’4’，按照ASCII码升序后组成的新字符串为1234abcd
```

### 机考2

```text
解析输入的字符串数组，提取出字符串中的时间戳信息，并且将字符串按照时间戳排序后，输出到控制台。  
 
输入描述  
第1行指定数组的size；  
 
第2行到第n+1行，每行为一个独立的字符串，n为size的值。  
 
每行的字符串由" / - : "和字母、数字组成，时间戳在字符串中的位置不确定，时间戳格式为：2019-01-01T07:30:20，表示2019年1月1日，7点30分20秒。时间为24小时制。  
 
输出描述  
将输入的字符串按照时间戳进行从小到大排序后，输出。符合如下规则：  
 
1、如果时间戳信息相同，按照字符串长度从小到大进行排序；  
 
2、如果长度相同，则按照从首字符开始的ASCII码值比较，从小到大进行排序；  
 
3、如果两个字符串完全一样，则只需要输出一个。  
 
补充说明  
考生不需要考虑时间格式不符合的情况。  
 
示例 1  

输入  
5  
my/2019-01-01T09:00:01  
my/2019-01-01T09:00:01  
abc/2018-12-24T08:00:00/test/you  
1/2018-12-24T08:00:00/test/Test1  
123/2018-12-24T08:00:09/test/me  
输出  
1/2018-12-24T08:00:00/test/Test1  
abc/2018-12-24T08:00:00/test/you  
123/2018-12-24T08:00:09/test/me  
my/2019-01-01T09:00:01  
说明  
每行字符串中如果存在多个时间戳，以第一个为准；时间戳固定为"yyyy-MM-dd'T'HH:mm:ss"的格式
```

## H公司

### 机考1

```text
输入描述：
第一行为N，表示访问历史日志的条数，。  
接下来N行，每一行为一个RESTful API的URL地址，约束地址中仅包含英文字母和连接符/，最大层级为10，每层级字符串最大长度为10。  
最后一行为层级L和要查询的关键字。  
  
输出描述  
输出给定层级上，关键字出现的频次，使用完全匹配方式（大小写敏感）。  
  
e.g.  
输入：  
5  
/hcompany/computing/no/one  
/hcompany/computing  
/hcompany  
/hcompany/cloud/no/one  
/hcompany/wireless/no/one  
2 computing  
  
输出：  
2
```

### 机考2

测试用例只通过了80%。机考，提交代码的时候没有提示哪些测试用例没通过，所以也没法调试具体是代码哪部分逻辑出错。

```text
给你一个字符串 s，字符串s首尾相连成一个环形 ，请你在环中找出 'o' 字符出现了偶数次最长子字符串的长度。  
  
输入描述  
输入是一串小写字母组成的字符串  
输出描述  
输出是一个整数  
  
补充说明  
1 <= s.length <= 5 x 10^5  
s 只包含小写英文字母  
  
示例：  
输入  
alolobo  
输出  
6  
说明  
最长子字符串之一是 "alolob"，它包含'o' 2个。  
  
输入  
looxdolx  
输出  
复制  
7  
说明  
最长子字符串是 "oxdolxl"，由于是首尾连接在一起的，所以最后一个 'x' 和开头的 'l'是连接在一起的，此字符串包含 2 个'o' 。  
  
输入  
bcbcbc  
输出  
6  
说明  
这个示例中，字符串 "bcbcbc" 本身就是最长的，因为  'o' 都出现了 0 次。
```

### 机考3

```text
孙悟空爱吃蟠桃，有一天趁着蟠桃园守卫不在来偷吃。已知蟠桃园有N颗桃树，每颗树上都有桃子，守卫将在H小时后回来。  
  
孙悟空可以决定他吃蟠桃的速度K（个/小时），每个小时选一颗桃树，并从树上吃掉K个，如果树上的桃子少于K个，则全部吃掉，并且这一小时剩余的时间里不再吃桃。  
  
孙悟空喜欢慢慢吃，但又想在守卫回来前吃完桃子。  
  
请返回孙悟空可以在H小时内吃掉所有桃子的最小速度K（K为整数）。如果以任何速度都吃不完所有桃子，则返回0。  
  
输入描述：  
第一行输入为N个数字，N表示桃树的数量，这N个数字表示每棵桃树上蟠桃的数量。  
第二行输入为一个数字，表示守卫离开的时间H。  
其中数字通过空格分割，N、H为正整数，每棵树上都有蟠桃，且0<N<10000，0<H<10000。  
  
输出描述：  
吃掉所有蟠桃的最小速度K，无解或输入异常时输出0  
  
以下是测试用例：  
 
输入：  
2 3 4 5  
4  
输出：  
5  
  
输入：  
2 3 4 5  
3  
输出：  
0  
  
输入：  
30 11 23 4 20  
6  
输出：  
23

类似题目： https://leetcode-cn.com/problems/koko-eating-bananas/description/
```

### 技术面手撕代码1

[21. 合并两个有序链表 - 力扣（LeetCode）](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

```text
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
```

### 技术面手撕代码2

[33. 搜索旋转排序数组 - 力扣（LeetCode）](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/)

```text
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
输入：nums = [4,5,6,7,0,1,2]， target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 = target <= 10^4
-104 <= 目标 <= 104
```

代码实现：

```java
class Solution {

    public int search(int[] nums, int target) {
        int len = nums.length;

        if (len == 1) {
            return nums[0] == target ? 0 : -1;
        }

        int k = this.findK(nums);

        if (target >= nums[0]) {
            return findTarget(nums, 0, len - k - 1, target);
        } else {// 从 len - k 的位置开始找
            return findTarget(nums, len - k, len - 1, target);
        }
    }

    private int findTarget(int[] nums, int left, int right, int target) {
        int index = Arrays.binarySearch(nums, left, right + 1, target);
        return index < 0 ? -1 : index;
    }

    private int findK(int[] nums) {
        int len = nums.length;

        if (nums[0] < nums[len - 1]) {// 从0旋转，还是升序
            return 0;
        }

        int left = 0;
        int right = len - 1;
        while (left != right - 1) {
            int mid = (right - left) / 2 + left;
            if (nums[mid] > nums[left]) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return len - right;
    }

}
```


### 技术面手撕代码3

```text
寿司店周年庆，正在举办优惠活动回馈新老客户。寿司转盘上总共有n盘寿司，prices[i]是第i盘寿司的价格，如果客户选择了第i盘寿司，寿司店免费赠送客户下一盘寿司j，前提是prices[j]<prices[i]，如果没有满足条件的j，则不赠送寿司。  
给你一个数组prices，返回一个数组，其中第i个元素存放着客户选择第i盘寿司后得到的寿司的总价格。  
 
1 <= prices.length <= 10^5  
1 <= prices[i] <= 10^3  
 
输入：prices = [8,4,6,2,3]  
输出：[12,6,8,2,5]  
 
输入：prices = [1,2,3,4,5]  
输出：[1,3,4,5,6]  
 
输入：prices = [10,1,1,6]  
输出：[11,1,1,7]
```

代码实现：
应该没有什么优化的空间了

```java
public class Main {
    public static void main(String[] args) {
        Main m = new Main();
        int[] p1 = new int[] {8,4,6,2,3};
        int[] p2 = new int[] {1,2,3,4,5};
        int[] p3 = new int[] {10,1,1,6};

        int[][] samples = new int[][] {p1, p2, p3};

        for (int i = 0; i < samples.length; i++) {
            System.out.println("p" + (i+1) + ":");
            int[] res = m.solution(samples[i]);
            for (int j = 0; j < res.length; j++) {
                System.out.print(res[j] + ",");
            }
            System.out.println();
        }

    }

    public int[] solution(int[] prices) {
        int len = prices.length;

        if (len == 1) {
            return prices;
        }
        int[] res = new int[len];

        for (int i = 0; i < len; i++) {
            int priceI = prices[i];

            int priceJ = findPriceJ(prices, priceI, i, len);

            res[i] = priceI + priceJ;
        }
        return res;
    }

    public int findPriceJ(int[] prices, int priceI, int i, int len) {
        //从i的右边开始找j
        for (int j = i + 1; j < len; j++) {
            if (prices[j] < priceI) {
                return prices[j];
            }
        }

        //右侧找不到j，从左侧开始找
        for (int j = 0; j < i; j++) {
            if (prices[j] < priceI) {
                return prices[j];
            }
        }
        return 0;
    }
}
```

## B公司

### 机考题

```text
给定一个字符串，统计每个字符的出现次数（不区分大小写），然后将字符按次数降序输出。如果字符的次数相同，则按字符升序输出。

例如：
输入：We Attack at Dawn
输出：atwcdekn
说明：a出现4次数最多，a首先输出；c和d都只出现了一次，但c在d前面，所以现输出c再输出d。
```



## 总结
总的来说，主要都是考一些基本的逻辑，没有考我比较头疼的动态规划之类的算法。 