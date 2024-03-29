# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCrawlerItem(scrapy.Item):
    id = scrapy.Field()
    topped = scrapy.Field()
    guid = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    isTop = scrapy.Field()
    referenceId = scrapy.Field()
    referenceImage = scrapy.Field()
    referenceName = scrapy.Field()
    referenceTime = scrapy.Field()
    referenceType = scrapy.Field()
    referenceTypeId = scrapy.Field()
    firstCategory = scrapy.Field()
    secondCategory = scrapy.Field()
    thirdCategory = scrapy.Field()
    replyCount = scrapy.Field()
    replyCount2 = scrapy.Field()
    score = scrapy.Field()
    status = scrapy.Field()
    title = scrapy.Field()
    usefulVoteCount = scrapy.Field()
    uselessVoteCount = scrapy.Field()
    userImage = scrapy.Field()
    userImageUrl = scrapy.Field()
    userLevelId = scrapy.Field()
    userProvince = scrapy.Field()
    viewCount = scrapy.Field()
    orderId = scrapy.Field()
    isReplyGrade = scrapy.Field()
    nickname = scrapy.Field()
    userClient = scrapy.Field()
    images = scrapy.Field()
    showOrderComment = scrapy.Field()
    mergeOrderStatus = scrapy.Field()
    discussionId = scrapy.Field()
    productColor = scrapy.Field()
    productSize = scrapy.Field()
    imageCount = scrapy.Field()
    integral = scrapy.Field()
    userImgFlag = scrapy.Field()
    anonymousFlag = scrapy.Field()
    userLevelName = scrapy.Field()
    plusAvailable = scrapy.Field()
    productSales = scrapy.Field()
    mobileVersion = scrapy.Field()
    aesPin = scrapy.Field()
    officialsStatus = scrapy.Field()
    excellent = scrapy.Field()
    recommend = scrapy.Field()
    userLevelColor = scrapy.Field()
    userClientShow = scrapy.Field()
    isMobile = scrapy.Field()
    days = scrapy.Field()
    afterDays = scrapy.Field()
