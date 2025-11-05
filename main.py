import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json as js


def main() -> None:
    with open("players.json", "r") as read_file:
        data = js.load(read_file)

        for name, values in data.items():

            race, _ = Race.objects.get_or_create(
                name=values["race"].get("name"),
                description=values["race"].get("description", ""))

            if values["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=values["guild"].get("name"),
                    defaults={
                        "description": values["guild"].get("description", "")
                    }
                )
            else:
                guild = None
            player, _ = Player.objects.get_or_create(
                nickname=name,
                defaults={"email": values["email"],
                          "bio": values["bio"],
                          "race": race,
                          "guild": guild
                          }
            )

            for skll in values["race"].get("skills"):
                skill, _ = Skill.objects.get_or_create(
                    name=skll["name"],
                    defaults={"bonus": skll["bonus"],
                              "race": race
                              }
                )


if __name__ == "__main__":
    main()
