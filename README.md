biqiuge.com
--
 ~~~~text
  使用scrapy 爬取笔趣小说 
  
  ~~~~

食用说明
--
+ 食用
```text
   git clone https://github.com/gsdukbh/biqu-scrapy.git
   cd biqu-scrapy
   cd my
   scrapy crawl biqu
 ```
+ 环境配置
 ```text
    redis 5, python3, scrapy, scrapy-redis ,MongoDB or MySql   
```
+ MySql 建表命令

```mysql
CREATE TABLE novel_list (
                            novel_id VARCHAR(50) primary key,
                            novel_name VARCHAR ( 50 ),
                            novel_author VARCHAR ( 50 ),
                            novel_type VARCHAR ( 20 ),
                            novel_info VARCHAR ( 500 ),
                            novel_cover VARCHAR ( 200 ),
                            novel_uptime VARCHAR ( 50 ),
                            novel_source VARCHAR ( 100 ),
                            index novel_list_novel_author_index(novel_author),
                            index novel_list_novel_name_index(novel_name),
                            index novel_list_novel_type_index(novel_type)
);
CREATE TABLE novel_chapter (
                               chapter_count int NOT NULL AUTO_INCREMENT primary key,
                               chapter_id int ,
                               novel_id VARCHAR(50),
                               chapter_title VARCHAR ( 50 ),
                               chapter_url VARCHAR ( 200 ),
                               chapter_content longtext,
                               index novel_chapter_chapter_id_index(chapter_id),
                               index novel_chapter_chapter_title_index(chapter_title),
                               index novel_chapter_novel_id_index(novel_id)
);


```
