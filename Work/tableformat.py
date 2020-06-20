def create_formatter(fmt):
    """
    Selects the type of format
    :param fmt:
    :return:
    """
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt},'
                           f' Supported formats : txt, csv, html')

    return formatter


class TableFormatter:
    """
    This is an abstract class for all the formater
    """
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings.
        '''

        for header in headers:
            print(f"{header:>10s}", end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''

        for data in rowdata:
            print(f"{data:>10s}", end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output the portfolio data in CSV format
    """

    def headings(self, headers):
        """
        Emit CSV headers
        :param headers:
        :return:
        """
        print(",".join(headers))

    def row(self, rowdata):
        """
        Emit CSV type row data
        :param rowdata:
        :return:
        """

        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output the portfolio data in HTML format
    """

    def headings(self, headers):
        """
        Emit HTML type header data
        :param headers:
        :return:
        """

        print("<tr>", end='')
        for header in headers:
            print(f"<th>{header}</th>", end='')
        print("</tr>")
        # print()

    def row(self, rowdata):
        """
        Emit HTML type row data
        :param rowdata:
        :return:
        """
        print("<tr>", end='')
        for data in rowdata:
            print(f"<td>{data}</td>", end='')
        print("</tr>")
        # print()


def print_table(objects, columns, fmt='txt'):
    """
    Prints a nicely formatted table with dyanmic colums
    :return:
    """
    formatter = create_formatter(fmt)
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, column)) for column in columns]
        formatter.row(rowdata)




