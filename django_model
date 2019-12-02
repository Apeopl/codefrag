class CheckSession(models.Model):
    taskId = models.IntegerField('质检任务标识')
    sessionId = models.CharField('会话唯一标识')
    sessionTags = models.CharField('会话标签', max_length=500)
    startTime = models.CharField('会话开始时间', null=True)
    closeTime = models.CharField('会话结束时间', null=True)
    remainTime = models.IntegerField('会话持续时间', default=0)
    agentNo = models.CharField('坐席编号')
    agentGroup = models.CharField('坐席分组')
    agentName = models.CharField('坐席名称')
    customName = models.CharField('客户名称')
    customLocal = models.CharField('客户地区')
    customReview = models.CharField('客户评价')
    closeByAgent = models.IntegerField('是否是客户关闭', default=0)
    matchKeywords = models.IntegerField('是否需要检查关键词', default=0)
    hasCheck = models.IntegerField('是否已完成检查', default=0)
    score = models.FloatField('对当前会话的评分', default=0)
    missNodeCount = models.IntegerField('遗漏节点数', default=0)
    violationRuleCount = models.IntegerField('当前质检会话的违规数', default=0)
    violationRules = models.CharField('违规规则列表', max_length=5000)
    checkResult = models.TextField('质检结果')
    processCheckResult = models.TextField('流程质检结果')
    note = models.CharField('标签分类，备注建议', max_length=500)
    conversationCount = models.IntegerField('此会话包含的消息数量', default=0)
    conversationList = models.TextField('此会话包含的对话消息')
    extra = models.CharField('此会话包含的额外消息', max_length=2000)
    scoreItemRecord = models.TextField('记录每个评分项的得分情况')
    createdAt = models.DateTimeField('创建时间', null=True)
    updatedAt = models.DateTimeField('更新时间', null=True)

    def __str__(self):
        return self.sessionId

    class Meta:
        abstract = True

    @classmethod
    def set_table(Class, table_name):
        class Meta:
            db_table = table_name

        attrs = {
            '__module__': Class.__module__,
            'Meta': Meta
        }
        return type(table_name, (Class,), attrs)

"""
数据库分表，Django orm model的编写和使用：
tn = CheckSession.set_table(table_name)
tn.objects.filter(**session_condition)
"""
