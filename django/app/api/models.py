from django.db import models

class VariantHeader(models.Model):
  variantKey = models.TextField()
  vairantName = models.CharField(max_length=64)
  description = models.TextField()
  def __str__(self):
    return self.variantName
  
class VariantItem(models.model):
  variantKey = models.ForeignKey(VariantHeader.variantKey, on_delete=models.CASCADE)
  fieldName = models.TextField()
  fieldDescription = models.ForeignKey()
  mandatory =  models.BooleanField()
  def __str__(self):
    return self.fieldName

  
class VariantItemValue(models.Model):
  variantKey = models.ForeignKey(VariantHeader.variantKey, on_delete=models.CASCADE)
  fieldName = models.ForeignKey(VariantItem.fieldName, on_delete=models.CASCADE)
  operation = models.TextField()
  keyField = models.TextField()
  value1 = models.TextField()
  value2 = models.TextField()

  def __str__(self):
    return f"{self.operation} {self.keyField}"