from rest_framework import serializers

# Para exponer API REST
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        # Importar el modelo dentro de la clase Meta
        from .models import Choice
        model = Choice
        fields = ["id", "choice_text"]

class PollSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    class Meta:
        from .models import Poll
        model = Poll
        fields = ["id", "question", "choices", "created_at"]

    def get_choices(self, obj):
        from .models import Choice
        return ChoiceSerializer(obj.choices.all(), many=True).data

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Vote
        model = Vote
        fields = ["poll", "choice", "user"]
