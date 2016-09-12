//
//  SystemMessageTableViewCell.m
//  scrollViewDamo
//
//  Created by 韩雪滢 on 9/11/16.
//  Copyright © 2016 小腊. All rights reserved.
//

#import "SystemMessageTableViewCell.h"

@interface SystemMessageTableViewCell()

@property (weak, nonatomic) IBOutlet UIImageView *messageImg;
@property (weak, nonatomic) IBOutlet UILabel *messageNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *messageContentLabel;
@property (weak, nonatomic) IBOutlet UILabel *messageUpdateLabel;



@end

@implementation SystemMessageTableViewCell

- (void)awakeFromNib {
    [super awakeFromNib];
    // Initialization code
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}


- (void)setMessageName:(NSString *)messageName{
    if(![_messageName isEqualToString:messageName]){
        _messageName = [messageName copy];
        _messageNameLabel.text = _messageName;
    }
}

- (void)setCircleURL:(NSString *)circleURL{
    if(![_circleURL isEqualToString:circleURL]){
        _circleURL = [circleURL copy];
        
        UIImage *circleImg = [UIImage imageWithData:[NSData dataWithContentsOfURL:[NSURL URLWithString:_circleURL]]];
        [self.messageImg setImage:[self OriginImage:circleImg scaleToSize:self.messageImg.bounds.size]];
        self.messageImg.layer.masksToBounds = YES;
        self.messageImg.layer.cornerRadius = self.messageImg.bounds.size.width / 2.0;
    }
}
- (void)setMessageContent:(NSString *)messageContent{
    if(![_messageContent isEqualToString:messageContent]){
        _messageContent = [messageContent copy];
        _messageContentLabel.text = _messageContent;
    }
}
- (void)setUpdateTime:(NSString *)updateTime{
    if(![_updateTime isEqualToString:updateTime]){
        _updateTime = [updateTime copy];
        _messageUpdateLabel.text = _updateTime;
    }
}
//改变图片的大小适应image View的大小
-(UIImage *)OriginImage:(UIImage *)image scaleToSize:(CGSize)size{
    UIGraphicsBeginImageContext(size);
    [image drawInRect:CGRectMake(0, 0, size.width, size.height)];
    UIImage *scaledImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return scaledImage;
}

@end