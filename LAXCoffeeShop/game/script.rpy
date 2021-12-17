# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾伦 莫里斯", image="ellen")
define l = Character("劳拉 哈里斯", image="lara")
define m = Character(("我"), color="#eb9534")


# 游戏在此开始。

label start:

    $ renpy.movie_cutscene("LAXIntro.webm")

    scene bg laview
    with fade
    play music "audio/The Midnight.mp3" fadein 1.0 fadeout 1.0
    
    "洛杉矶。"
    "爱乐之城。"
    "阳光之城"
    "承载着加利福尼亚的无垠阳光"
    "一片享乐与繁荣的圣地"
    "山脉，{w}城市，{w}海滩，{w}好莱坞，{w}迪士尼乐园......"   
    "无数游客来到这里"
    "只为了能在这里花天酒地，纸醉金迷"
    "而坐落在洛杉矶西北面的"
    "是洛杉矶的交通枢纽之一"


    scene bg lax outside
    with fade
    
    "洛杉矶国际机场"
    "作为西海岸最繁忙的机场"
    "这14平方公里的土地孕育了太多的故事"
    "工作、生活、娱乐，一切在这里混合"
    "行色匆匆的人们在机场里穿行"

    scene bg lax hall
    with fade

    "而在这一片繁荣的中心"
    "机场外圈的西南角"
    "有一家小小的咖啡厅"
    "店外只有一块不显眼的标牌"
    "经常旅行的人经常会匆匆路过"
    "但绝不会多看一眼"


    scene bg coffee
    with fade
    "很多“闯入”这间咖啡厅的人都会对他们家咖啡之便宜而惊讶"
    "时不时还会有咖啡师对他们家的经典咖啡啧啧称叹"
    "但是很少会有人问一句"
    "“你们是怎么在洛杉矶这片昂贵的土地上存活的？”"
    "店长总是微微一笑，沉默不语，双手递上一杯卡布奇诺"

    m "而这位店长，便是本人"
    m "我有很多故事想要跟你讲"
    m "我也完全可以告诉你我们存活至今的秘密"
    m "但这些并不重要"
    m "重要的是在洛杉矶国际机场"
    m "有这样一家咖啡厅"
    m "等待任何迷路的旅客前来拜访"
    m "喝一杯温暖的卡布奇诺"
    m "让所有人宾至如归"
    m "欢迎来到LAX COFFEE"

    jump chapterOne

    # 此处为游戏结尾。

    return

label chapterOne:

    scene bg coffee
    with fade
    play music "audio/Los Angeles.mp3" fadein 1.0 fadeout 1.0 volume 0.3

    "八月十二日 2019年 13:00 PST "
    
    play sound "audio/doorbell.mp3"
    pause 2.0
    m "欢迎光临"
    show ellen at center with dissolve
    "一位扎着丸子头，穿着休闲夹克与黑色连帽卫衣的女性走进了咖啡厅"
    "丸子头女生" "你好啊！"
    "跟着这个丸子头女生走进咖啡厅的，是另一位稍矮一些的女生"
    show ellen at left with ease
    show lara at center with dissolve
    "稍矮的女生" "你好，你好！"
    "丸子头女生" "你好啊！"
    "稍矮的女生" "其实说来惭愧，我们刚下飞机...人生地不熟"
    "稍矮的女生" "这附近最近的杂货店(grocery)在哪里呢...?"
    m "（其实我也不是很熟啊）"
    m "（用手机查一下吧...）"
    "请善用搜索引擎等工具游玩本游戏"

    python:
        ifAnswerCorrect = False;
        GroceryName = renpy.input("离洛杉矶国际机场(LAX)最近的杂货店(Grocery)叫什么呢？(输入英文)", length=32)
        if str.lower(GroceryName) =="ralphs" or str.lower(GroceryName) == "vons":
            ifAnswerCorrect = True;
    

    "丸子头女生" "[GroceryName] 是吗？谢谢你！"
    e "哦忘记介绍我自己了。我是艾伦。艾伦莫里斯。"
    e "这位是我的朋友罗拉 哈里斯。"
    
    menu:

        "你好啊，欢迎来到洛杉矶":
            pass

label chitchat:
    
    l "能给我们来一杯饮料吗"
    m "可以女士，您想来点啥？"
    "..."
    l "我们想在洛杉矶逛逛，有什么推荐的景点吗？"

    python:
        def LookupDic(name):
            SpotName_lookup = {
                'universal resort': '我推荐你去环球影城逛一逛。即使你不想买票，也可以去CityWalk玩一玩，买点纪念品。',
                'universal': '我推荐你去环球影城逛一逛。即使你不想买票，也可以去CityWalk玩一玩，买点纪念品。',
                'universal studio': '我推荐你去环球影城逛一逛。即使你不想买票，也可以去CityWalk玩一玩，买点纪念品。',

                'griffith park': '格里斐斯公园你了解吗？如果你喜欢绿树环绕的自然风格，请一定要去拜访一下。',
                'griffith': '格里斐斯公园你了解吗？如果你喜欢绿树环绕的自然风格，请一定要去拜访一下。',

                'hollywood': '没去过好莱坞，可不算来过洛杉矶。',
                'hollywood walk': '没去过好莱坞，可不算来过洛杉矶。',
                'hollywoodwalk': '没去过好莱坞，可不算来过洛杉矶。',

                'grand central': '你有去过大中央市场吗？虽然不算是景点，但是那里有很多只能在那儿才能吃到的美食。',
                'grandcentral': '你有去过大中央市场吗？虽然不算是景点，但是那里有很多只能在那儿才能吃到的美食。',
                'grand central market': '没你有去过大中央市场吗？虽然不算是景点，但是那里有很多只能在那儿才能吃到的美食。',
                
                'disney': '你去过迪士尼乐园吗？没去过的话可以去看看。',
                'disney resort': '你去过迪士尼乐园吗？没去过的话可以去看看。',
                'disneyland': '你去过迪士尼乐园吗？没去过的话可以去看看。'
            }
            print SpotName_lookup.get(name,name)
            return SpotName_lookup.get(name,name)

        recommemdation = str.lower(renpy.input("有什么可以推荐的景点吗(输入英文)", length=32))
        recommendation_say = LookupDic(recommemdation)

    m "[recommendation_say]"

    python:
        if recommemdation == "disney":
            renpy.jump ("disney")
        if recommemdation == "universal":
            renpy.jump ("universal")


label disney:
    scene bg coffee
    with fade

    show ellen at left with dissolve
    show lara at center with dissolve
    "三天后..."
    "熟悉的丸子头女生推门走进了咖啡厅"
    m "你好啊！谢谢你介绍我们去迪士尼！"
    l "我们一直想找个合适的时机，说出心中最真实的想法"
    m "昨天，我们终于明白了互相的心意......"

    "End of Demo"

    return

label universal:
    scene bg coffee
    with fade

    show ellen at left with dissolve
    show lara at center with dissolve
    "三天后..."
    "熟悉的丸子头女生推门走进了咖啡厅"
    m "你好啊！环球影城真的很好玩——"
    l "虽然这个时间的人有点多"
    m "但是还是很有意思的"

    "End of Demo"
    return


        





