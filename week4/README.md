brief description:
starting from the root page it operates depth first search.
you can specify suffix to include and exclude, and the depth of dfs.



Usage

```
$ python wiki.py
enter the following;  root - the page you start search from;  suffix - searches only pages with the suffix;  exclude_suffix - searches only pages without the suffix
root: 自然科学
suffix: 学
exclude_suffix: 大学
max_depth: 3

```
sample output

```
|-自然科学 (5100)
  |-アラビア科学 (145307)
  |-スコラ学 (20926)
  |-人文科学 (9504)
  |-化学 (671)
  |-医学 (75)
  |-地球科学 (2620)
  |-基礎科学 (84660)
  |-境界科学 (1301114)
  |-天文学 (516888)
  |-宗教哲学 (151131)
  |-工学 (7189)
  |-形式科学 (827322)
  |-心の哲学 (105875)
  |-応用科学 (84665)
  |-数学 (142)
  |-数学の哲学 (771315)
  |-数理科学 (314129)
  |-文化科学 (683259)
  |-文学 (64)
```