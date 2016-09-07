//
//  DemoVC5.m
//  Alumn
//
//  Created by Dorangefly Liu on 16/8/28.
//  Copyright © 2016年 刘龙飞. All rights reserved.
//


#import "DemoVC5.h"

#import "DemoVC5CellTableViewCell.h"

#import "SDRefresh.h"

#import "UITableView+SDAutoTableViewCellHeight.h"

#import "CircleViewController.h"

#import "Circle+Extension.h"

#import "User.h"

#import "AFNetManager.h"


@interface DemoVC5 ()


@property (nonatomic, strong) NSMutableArray *modelsArray;

@end

@implementation DemoVC5


{
    SDRefreshFooterView *_refreshFooter;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
  
    
    NSNumber *i=[[NSNumber alloc]initWithInt:1];
    [self creatModelsWithCount:4 page:i];
    
    __weak typeof(self) weakSelf = self;
    
    // 上拉加载
    _refreshFooter = [SDRefreshFooterView refreshView];
    [_refreshFooter addToScrollView:self.tableView];
    __weak typeof(_refreshFooter) weakRefreshFooter = _refreshFooter;
    _refreshFooter.beginRefreshingOperation = ^() {
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
            NSNumber *newpage=[[NSNumber alloc]initWithInt:page];
            NSDictionary *userInfo =[[NSDictionary alloc] initWithObjectsAndKeys:@"57c69d68d36ef3151eb80bac",@"topic_id",@"4",@"count",newpage,@"page",@"0",@"order", nil];
            NSDictionary *postdic = [[NSDictionary alloc] initWithObjectsAndKeys: [AFNetManager dictionaryToJson:userInfo],@"info_json",[User getXrsf],@"_xsrf", nil];
            NSLog (@"%@",postdic);
   
            [Circle circeDynamicListWithParameters:postdic page:newpage];
            [weakSelf creatModelsWithCount:4 page:newpage];
            [weakSelf.tableView reloadData];
            [weakRefreshFooter endRefreshing];
            
        });
    };
}



- (void)creatModelsWithCount:(NSInteger)count page:(NSNumber *) pages
{
    
    if (!_modelsArray) {
        _modelsArray = [NSMutableArray new];
    }
    
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *plistPath1= [paths objectAtIndex:0];
    NSString *plistName =[[NSString alloc] initWithFormat:@"DynamicList%@.plist",pages];
    NSString *fileName = [plistPath1 stringByAppendingPathComponent:plistName];
    NSArray *dictArray = [NSArray arrayWithContentsOfFile:fileName];
     NSMutableArray *models = [NSMutableArray arrayWithCapacity:[dictArray count]];
    for (NSDictionary *dict in dictArray) {
        DemoVC5Model *mod = [DemoVC5Model modelWithDict:dict];
        [self.modelsArray  addObject:mod];
    }
    page++;
  
  }


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    // >>>>>>>>>>>>>>>>>>>>> * cell自适应步骤1 * >>>>>>>>>>>>>>>>>>>>>>>>
    
    [self.tableView startAutoCellHeightWithCellClass:[DemoVC5CellTableViewCell class] contentViewWidth:[UIScreen mainScreen].bounds.size.width];
    
    
    return self.modelsArray.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *ID = @"test";
    DemoVC5CellTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:ID];
    if (!cell) {
        cell = [[DemoVC5CellTableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:ID];
    }
    cell.model = self.modelsArray[indexPath.row];
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    // >>>>>>>>>>>>>>>>>>>>> * cell自适应步骤2 * >>>>>>>>>>>>>>>>>>>>>>>>
    /* model 为模型实例， keyPath 为 model 的属性名，通过 kvc 统一赋值接口 */
    return [self.tableView cellHeightForIndexPath:indexPath model:self.modelsArray[indexPath.row] keyPath:@"model"];
}

-(void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    //该方法响应列表中行的点击事件
    NSLog(@"waht the Fuck");
    UIStoryboard *sb = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
   CircleViewController *VC = [sb instantiateViewControllerWithIdentifier:@"jump"];
    [self showViewController:VC sender:nil];
  
}

+(void) setID:(NSString *)id
{
    ID = id;
}

+(NSString *) getID
{
    extern NSString *ID;
    return ID;
}


@end