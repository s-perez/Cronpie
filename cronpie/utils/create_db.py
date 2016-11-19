from cronpie.models import Command, Run, Measure, database


database.connect()
database.create_tables([Command, Run, Measure], safe=True)
