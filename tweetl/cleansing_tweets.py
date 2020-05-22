import pandas as pd
import json
import re
import emoji
import mojimoji
import neologdn

class CleansingTweets:

    # replace and\s to space
    def cleansing_space(self, text):
        return re.sub("\u3000|\s", " ", text)

    # remove hashtags
    def cleansing_hash(self, text):
        return re.sub("#[^\s]+", "", text)

    # remove URLs
    def cleansing_url(self, text):
        return re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" , text)

    # remove pictograph
    def cleansing_emoji(self, text):
        return ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)

    # remove mention
    def cleansing_username(self, text):
        return re.sub(r"@([A-Za-z0-9_]+) ", "", text)

    #  remove image string
    def cleansing_picture(self, text):
        return re.sub(r"pic.twitter.com/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]*", "" , text)

    # unify characters.
    def cleansing_unity(self, text):
        text = text.lower()
        text = mojimoji.zen_to_han(text, kana=True)
        text = mojimoji.han_to_zen(text, digit=False, ascii=False)
        return text

    # replace number to zero
    def cleansing_num(self, text):
        text = re.sub(r'\d+', "0", text)
        return text

    # remove rt
    def cleansing_rt(self, text):
        return re.sub(r"RT @[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]*?: ", "" , text)

    def cleansing_text(self, text):
        text = self.cleansing_rt(text)
        text = self.cleansing_hash(text)
        text = self.cleansing_space(text)
        text = self.cleansing_url(text)
        text = self.cleansing_emoji(text)
        text = self.cleansing_username(text)
        text = self.cleansing_picture(text)
        text = self.cleansing_unity(text)
        text = self.cleansing_num(text)
        text = neologdn.normalize(text)
        return text

    def cleansing_df(self, df, subset_cols=["text"]):
        if "text" in subset_cols:
            # remove duplicates (because they might be RT.)
            df = df.drop_duplicates(subset="text", keep=False)

        df_copy = df.copy()

        for col in subset_cols:
            # cleansing
            df_copy[col] = df[col].apply(lambda x: self.cleansing_text(x))
            
        if "text" in subset_cols:
            # remove duplicates
            df_copy = df_copy.drop_duplicates(subset="text", keep=False).reset_index(drop=True)

        return df_copy
