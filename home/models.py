from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position_choices = [
        ('Forward', 'Forward'),
        ('Centre', 'Centre'),
        ('Defence', 'Defence'),
        ('Goalie', 'Goalie'),
    ]
    position = models.CharField(max_length=20, choices=position_choices)

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateField()
    half_length = models.IntegerField(help_text='Duration of each half in minutes')
    substitution_interval = models.IntegerField(help_text='Interval for substitutions in minutes')
    field_players_count = models.IntegerField(help_text='Number of players on the field at a time')

class Substitution(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_out = models.ForeignKey(Player, related_name='out_substitutions', on_delete=models.CASCADE)
    player_in = models.ForeignKey(Player, related_name='in_substitutions', on_delete=models.CASCADE)
    time = models.TimeField()
    period = models.CharField(max_length=10, choices=[('first', 'First Half'), ('second', 'Second Half')])

    def __str__(self):
        return f"{self.player_out} out, {self.player_in} in at {self.time} - {self.period}"

