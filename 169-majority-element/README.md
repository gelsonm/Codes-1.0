<h2><a href="https://leetcode.com/problems/majority-element/">169. Majority Element</a></h2><h3>Easy</h3><hr><div><p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>⌊n / 2⌋</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</div>

### Solution:

####  Approach 1: Using collections.Counter()

```python
from collections import Counter

def majorityElement(nums):
    # Count the occurrences of each element in the array
    count = Counter(nums)
    
    # Find the element with the most occurrences
    majority_element = max(count, key=count.get)
    
    return majority_element
```
**Time Complexity**: O(n) as we are iterating through the array once.
<br>
**Space Complexity**: O(n) as we are using a dictionary to store the count of each element in the array.

#### Approach 2: Sorting the array
```python
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
```
**Time Complexity**: O(nlogn) as we are sorting the array.
<br>
**Space Complexity**: O(1) as we are not using any additional data structure.

#### Approach 3: "Boyer-Moore Voting Algorithm"


```python
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
```
**Time Complexity**: O(n) as we are iterating through the array once.
<br>
**Space Complexity**: O(1) as we are only using a few variables to store the count and candidate element.
