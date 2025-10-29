import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        dados_json = json.load(file)

    for nickname, dados in dados_json.items():
        race, _ = Race.objects.get_or_create(
            name=dados["race"].get("name"),
            defaults={"description": dados["race"].get("description")},
        )

        for skill_data in dados["race"].get("skills"):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race,
            )

        if dados.get("guild"):
            desc = dados["guild"].get("description")
            guild, _ = Guild.objects.get_or_create(
                name=dados["guild"].get("name"),
                defaults={"description": desc},
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=dados.get("email"),
            bio=dados.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
