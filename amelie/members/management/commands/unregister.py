from datetime import date

from django.core.management.base import BaseCommand
from django.utils.encoding import smart_str

from amelie.members.models import Membership
from amelie.tools.logic import current_association_year


class Command(BaseCommand):
    args = 'unregister'
    help = "Unregisters people with a study long membership who are not a student any more."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser=parser)
        parser.add_argument(
            '--commit',
            action='store_true',
            dest='commit',
            default=False,
            help='Save changes'
        )

    def handle(self, *args, **options):
        if len(args) != 2:
            print("Not enough args! You need 2: inputfile outputfile")
            return

        inputfile = args[0]
        outputfile = args[1]

        current_year = current_association_year()

        memberships = Membership.objects.filter(year=current_year, type__name_en__in=['Studylong (continuation)', 'Studylong (first year)'], ended__isnull=True)

        commit = options['commit']

        if not commit:
            self.stdout.write('** TEST MODE **')
            self.stdout.write('Add --commit to save changes')

        tcsbitlist = []

        student_numbers_file = open(inputfile, 'r')
        for line in student_numbers_file:
            line = line.strip()
            try:
                tcsbitlist.append(int(line))
            except ValueError:
                self.stderr.write('"%s" is not a valid student number' % line)
        student_numbers_file.close()

        # The people in this file did not automatically get a new membership.
        discontinued_members_file = open(outputfile, 'w')

        for membership in memberships:
            try:
                if membership.member.student and membership.member.student.number in tcsbitlist:
                    # OK
                    pass
                else:
                    membership.ended = date.today()
                    self.stdout.write("%s %s (%s) is being unregistered" % (smart_str(membership.member.first_name), smart_str(membership.member.last_name), smart_str(membership.type.name)))

                    if membership.member.last_name_prefix:
                        discontinued_members_file.write("%s, %s %s, %s, %s\n" % (smart_str(membership.member.first_name), smart_str(membership.member.last_name_prefix), smart_str(membership.member.last_name), smart_str(membership.member.email_address), smart_str(membership.type.name)))
                    else:
                        discontinued_members_file.write("%s, %s, %s, %s\n" % (smart_str(membership.member.first_name), smart_str(membership.member.last_name), smart_str(membership.member.email_address), smart_str(membership.type.name)))

                    if commit:
                        membership.save()

            except Exception:
                import traceback
                traceback.print_exc()

        discontinued_members_file.close()
