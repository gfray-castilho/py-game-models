import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        dados_json = json.load(file)

    for nickname, dados in dados_json.items():
        race, _ = Race.objects.get_or_create(
            name=dados["race"]["name"],
            defaults={"description": dados["race"]["description"]},
        )

        for skill_data in dados["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )

        if dados["guild"]:
            desc = dados["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=dados["guild"]["name"],
                defaults={"description": desc},
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=dados["email"],
            bio=dados["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
