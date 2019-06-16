import re


class GlobalData:
    # fi:file input
    @property
    def fi_texture_type(self):
        return 1

    @property
    def fi_atlas_type(self):
        return 3

    @property
    def fi_mesh_type(self):
        return 2

    # td tree id find
    @property
    def td_list_item(self):
        return False

    @property
    def td_single(self):
        return True

    @property
    def td_texture_type(self):
        return 0

    @property
    def td_mesh_type(self):
        return 1

    @property
    def td_atlas_type(self):
        return 2

    @property
    def td_region_type(self):
        return 3

    @property
    def td_view_type(self):
        return 4

    # tree_filter
    @property
    def tf_all(self):
        return 0

    @property
    def tf_default_skin_only(self):
        return 1

    @property
    def tf_char_texture_only(self):
        return 1

    @property
    def tf_skin_only(self):
        return 2

    @property
    def tf_NPC_only(self):
        return 2

    @property
    def tf_build_up_only(self):
        # 仅改造
        return 3

    @property
    def tf_enemy_only(self):
        return 3

    @property
    def tf_wedding_only(self):
        # 婚纱
        return 4

    @property
    def tf_char_painting_only(self):
        return 4

    @property
    def tf_young_only(self):
        return 5

    @property
    def tf_char_build_up_only(self):
        return 5

    @property
    def tf_char_skin_only(self):
        return 6

    # fp:filter pattern
    @property
    def fp_all(self):
        return re.compile(r'^.+$')

    # @property
    # def fp_default_skin(self):
    #     return re.compile(r'^.+(?<!_[\dhg])$')

    # @property
    # def fp_skin(self):
    #     return re.compile(r'^.+(?<=_\d)$')

    # @property
    # def fp_build_up(self):
    #     return re.compile(r'^.+(?<=_g)$')

    # @property
    # def fp_wedding(self):
    #     return re.compile(r'^.+(?<=_h)$')

    # @property
    # def fp_young(self):
    #     return re.compile(r'^.+_younv(?:_[\dhg])?$')

    # @property
    # def fp_pattern_group(self):
    #    return self.fp_all, self.fp_default_skin, self.fp_skin, self.fp_build_up, self.fp_wedding, self.fp_young

    @property
    def fp_char_texture(self):
        return re.compile(r"^(?:build_char_|char_)\d{3}_.+(?<=#\d)?$")

    @property
    def fp_npc(self):
        return re.compile(r'^npc_\d{3}_[^_]+$')

    @property
    def fp_enemy(self):
        return re.compile(r'^enemy_\d{4}_.+$')

    @property
    def fp_char_painting(self):
        return re.compile(r'^char_\d{3}_[^_]+_1$')

    @property
    def fp_char_build_up(self):
        return re.compile(r'^char_\d{3}_[^_]+_[12][+b]?(?<!_1)$')

    @property
    def fp_char_skin(self):
        return re.compile(r"^char_\d{3}_.+(?<=#\d)$")

    @property
    def fp_pattern_group(self):
        return self.fp_all, self.fp_char_texture, self.fp_npc, self.fp_enemy, self.fp_char_painting, \
               self.fp_char_build_up, self.fp_char_skin

    # et:export type
    @property
    def et_all(self):
        return 0

    @property
    def et_copy_only(self):
        return 1

    @property
    def et_select(self):
        return 2

    @property
    def et_list_item(self):
        return 3

    # fif:file input filter
    @property
    def fif_all(self):
        return 0

    @property
    def fif_default_skin_only(self):
        return 1

    @property
    def fif_skin_only(self):
        return 2

    @property
    def fif_build_up_only(self):
        return 3

    @property
    def fif_wedding_only(self):
        return 4

    @property
    def fif_young_only(self):
        return 5

    # mrfz
    @property
    def fif_char_texture(self):
        return 1

    @property
    def fif_npc(self):
        return 2

    @property
    def fif_enemy(self):
        return 3

    @property
    def fif_char_painting(self):
        return 4

    @property
    def fif_char_build_up(self):
        return 5

    @property
    def fif_char_skin(self):
        return 6

    # feg :file export group
    @property
    def feg_do_no_group(self):
        return 0

    @property
    def feg_by_name(self):
        return 1

    @property
    def feg_by_type(self):
        return 2

    @property
    def feg_by_is_able(self):
        return 3

    # sk:setting_keys
    @property
    def sk_clear_when_input(self):
        return "input_clear"

    @property
    def sk_input_filter_tex(self):
        return "input_filter_tex"

    @property
    def sk_input_filter_mesh(self):
        return "input_filter_mesh"

    @property
    def sk_input_filter(self):
        return "input_filter"

    @property
    def sk_output_group(self):
        return "output_group"

    @property
    def sk_use_cn_name(self):
        return "use_cn"

    @property
    def sk_skip_exist(self):
        return "skip_exist"

    @property
    def sk_open_output_dir(self):
        return "open_dir"

    @property
    def sk_finish_exit(self):
        return "finish_exit"

    @property
    def sk_make_new_dir(self):
        return "make_new_dir"

    @property
    def sk_export_all_while_copy(self):
        return "export_copy"

    @property
    def sk_auto_search(self):
        return "auto_search"

    @property
    def sk_inverse(self):
        return "inverse"

    @property
    def sk_regex_search(self):
        return "regex_search"

    # image resize type:irt
    @property
    def irt_default(self):
        return 0

    @property
    def irt_scale(self):
        return 1

    @property
    def irt_resize(self):
        return 2
