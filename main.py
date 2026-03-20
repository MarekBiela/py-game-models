import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race = Race.objects.get_or_create(
            name=player_data.get("race", {}).get("name"),
            defaults={
                "description": player_data.get("race", {}).get("description")
            }
        )[0]
        for skill in player_data.get("race", {}).get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": race}
            )
        guild = None
        if player_data.get("guild"):
            guild = Guild.objects.get_or_create(
                name=player_data.get("guild", {}).get("name"),
                defaults={
                    "description":
                        player_data.get("guild", {}).get("description")
                }
            )[0]
        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
