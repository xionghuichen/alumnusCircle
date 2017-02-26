todo list:
- 登陆
	- api登陆操作[ok]
- 注册
	- api验证手机号[ok]
	- api获取手机验证码
	- api登陆[ok]
- 退出登陆
	- api退出
- 我:
	- [?]api 查看个人信息
		- 信息:头像[登陆的时候获得]
	- api 修改资料
		- 上传新消息[]
	- [?]api 我的圈子列表--->关注.[创建,管理]
		- 信息:
			- 我创建.管理的圈子.
			- 圈子的名称,圈子的头像.
	- api 我收藏的名片列表:
		- 信息:我的关注列表.
- 信息:
	- 通知:
		- 信息:
			- [api] 获取用户当前的消息列表
		- [api] 发送同意,拒绝圈子加入申请
			- 信息:
				- 圈子id
				- 处理结果
				- 被处理人id
	- 私信:
	- [api] 我的评论列表:
		- 信息:
			- 友盟获取我收到的评论列表
- 发现圈子:
	- 圈子类型列表
		- 信息:
			- [api] 友盟,类别下的话题列表
		- 某一个类别的圈子列表
            - [api] 申请加入圈子:
                - 信息:
                    - 发送加入圈子理由
                    - 发送圈子id
                    - 圈子介绍
                    - 圈子头像
                    - 圈子名称
            - 联系我:
            	- [api] 发布feed,
            	- 关联话题 虚拟圈子id
- 人脉:
	- [api] 获取最新注册的用户列表
		-信息
			- 获取个数
			- 获取的页码
		[api]- 进行,院系,年份,城市筛选.
	- [api] 搜索
- 首页:
	-  信息:
		- [api] 友盟获取我关注的圈子列表
	- 进入圈子详情页面
		- 信息:
			- [api][友盟]圈子动态列表
				- [api]点赞
				- [api]评论
				- [api]发表评论
				- 封面url.
				- 发布人的头像,姓名,入学年份,职业,城市专业.
				- [api] 动态详情
		- [api] 圈子成员列表
			- [成员列表]:友盟圈子的关注列表
				- 头像
				- 名字
				- 入学年份,职业,城市专业
		- [2.0] 群聊
		- [2.0] 分享
		- [api] 发布动态
			- 信息:
				- [友盟]发布feed接口
				- 圈子id[realid]
		- 联系我
			- [友盟]获取圈子动态列表
			- 使用virtual 动态列表
		- 设置
			- [api]设置圈子头像, 名称,设置圈子介绍
				- 信息:
					- 友盟api:编辑话题
			-[api]:  设置圈子管理员:
				- 信息:
					- 通知模块.
					- 管理员id list.
					- 圈子id.
				- 获取圈子的管理员
			- [api]: 踢出群成员
				- 信息:
					- 成员id
					- 后台利用这个id来访问umeng接口, 模拟该用户的accesstoken来进行取消关注动态的操作,并且删除该用户的my circle list
			- [api]: 退出圈子
				- 信息:
					- 成员id
					- 取消关注,删除用户的my circle list

后台api优先级：从低到高。5是最高
1.  圈子设置
2. 	圈子的创建和申请
3. 	动态发表，联系我
3. 	圈子，动态， 人脉， 消息，我的信息的获取
4. 	登陆注册


需要前台处理的逻辑：
1. 维护一些全局变量： my_circle_list update_time 等。
2. 请求的preprocess处理逻辑


9.5 - 9.6 [圈子体系，人脉体系 集成]
给圈子类型
获取圈子类型列表
获取我加入的圈子列表[申请加入圈子]
获取圈子的成员列表[申请加入圈子]
点开查看圈子的动态。[动态发布]

登录
注册.
人脉详情.
高级筛选.


9.7-9.8  [消息体系，与我相关的体系集成]

9.9-9.10 [头像，]

