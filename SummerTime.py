class SummerTime:
    def lex_rank_analysis(self, parser_configuration, number_of_lines_to_update)
        from sumy.summarizers.lex_rank import LexRankSummarizers
        summarizer = LexRankSummarizer()
        summarization_results = summarizer(parser_configuration.document, number_of_lines_to_output)
        print("\nBegin Raw summary from LexRank\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw summary from LexRank\n")

        return summarization_results
    def lsa_analysis(self, parser_configuration, number_of_lines_to_output):
        from summy.summarizers.lsa import LsaSummarizer
        