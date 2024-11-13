from django.db import models

# Create your models here.

# class Companion(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f"{self.user.username} - {self.trip.start_location} - {self.trip.end_location}"


# @receiver(post_save, sender=Companion)
# def decrease_seats_available(sender, instance, created, **kwargs):
#     if created:
#         trip = instance.trip
#         user_wallet = Wallet.objects.filter(user=instance.user)
#         if trip.seats_available > 0:
#             trip.seats_available -= instance.seets
#             trip.save()