"""init

Revision ID: d9b5fad5efe5
Revises: d6a842a8252e
Create Date: 2023-12-06 22:23:38.427369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd9b5fad5efe5'
down_revision: Union[str, None] = 'd6a842a8252e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_t_perm_label_id', table_name='t_perm_label')
    op.drop_table('t_perm_label')
    op.drop_index('ix_t_users_id', table_name='t_users')
    op.drop_index('ix_t_users_username', table_name='t_users')
    op.drop_table('t_users')
    op.drop_index('ix_t_menus_id', table_name='t_menus')
    op.drop_table('t_menus')
    op.drop_index('ix_t_hiker_developer_id', table_name='t_hiker_developer')
    op.drop_table('t_hiker_developer')
    op.drop_index('ix_t_user_role_id', table_name='t_user_role')
    op.drop_table('t_user_role')
    op.drop_index('ix_t_config_settings_id', table_name='t_config_settings')
    op.drop_index('ix_t_config_settings_name', table_name='t_config_settings')
    op.drop_table('t_config_settings')
    op.drop_index('ix_t_hiker_rule_id', table_name='t_hiker_rule')
    op.drop_table('t_hiker_rule')
    op.drop_index('ix_t_dict_details_id', table_name='t_dict_details')
    op.drop_table('t_dict_details')
    op.drop_index('ix_t_role_menu_id', table_name='t_role_menu')
    op.drop_table('t_role_menu')
    op.drop_index('ix_t_hiker_rule_type_id', table_name='t_hiker_rule_type')
    op.drop_table('t_hiker_rule_type')
    op.drop_index('ix_t_dict_data_dict_type', table_name='t_dict_data')
    op.drop_index('ix_t_dict_data_id', table_name='t_dict_data')
    op.drop_table('t_dict_data')
    op.drop_index('ix_t_perm_label_role_id', table_name='t_perm_label_role')
    op.drop_table('t_perm_label_role')
    op.drop_index('ix_t_roles_id', table_name='t_roles')
    op.drop_index('ix_t_roles_key', table_name='t_roles')
    op.drop_table('t_roles')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_roles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('key', mysql.VARCHAR(collation='utf8mb4_bin', length=64), nullable=False, comment='权限标识'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("''"), nullable=True, comment='权限名称'),
    sa.Column('order_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='顺序'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态(0: 正常, 1: 停用)'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_roles_key', 't_roles', ['key'], unique=False)
    op.create_index('ix_t_roles_id', 't_roles', ['id'], unique=False)
    op.create_table('t_perm_label_role',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('label_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_perm_label_role_id', 't_perm_label_role', ['id'], unique=False)
    op.create_table('t_dict_data',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('dict_type', mysql.VARCHAR(collation='utf8mb4_bin', length=64), nullable=False, comment='字典类型'),
    sa.Column('dict_name', mysql.VARCHAR(collation='utf8mb4_bin', length=64), server_default=sa.text("''"), nullable=True, comment='字典名称'),
    sa.Column('remark', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("''"), nullable=True, comment='备注'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态 0: 正常  1:停用'),
    sa.Column('order_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='排序'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_dict_data_id', 't_dict_data', ['id'], unique=False)
    op.create_index('ix_t_dict_data_dict_type', 't_dict_data', ['dict_type'], unique=False)
    op.create_table('t_hiker_rule_type',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=False, comment='分类名称'),
    sa.Column('count_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='数目'),
    sa.Column('active', mysql.TINYINT(display_width=1), server_default=sa.text('1'), autoincrement=False, nullable=True, comment='是否启用'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_hiker_rule_type_id', 't_hiker_rule_type', ['id'], unique=False)
    op.create_table('t_role_menu',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('menu_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_role_menu_id', 't_role_menu', ['id'], unique=False)
    op.create_table('t_dict_details',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('dict_label', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=False, comment='字典标签'),
    sa.Column('dict_disabled', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=False, comment='是否禁用'),
    sa.Column('dict_value', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=False, comment='字典键值'),
    sa.Column('remark', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("''"), nullable=True, comment='备注'),
    sa.Column('is_default', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=False, comment='是否默认值'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态 0: 正常  1:停用'),
    sa.Column('order_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='排序'),
    sa.Column('dict_data_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_dict_details_id', 't_dict_details', ['id'], unique=False)
    op.create_table('t_hiker_rule',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='规则名称'),
    sa.Column('type_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='规则类型'),
    sa.Column('dev_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='开发者'),
    sa.Column('value', mysql.TEXT(collation='utf8mb4_bin'), nullable=True, comment='规则Json'),
    sa.Column('url', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='地址'),
    sa.Column('state', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态'),
    sa.Column('auth', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='私有密码'),
    sa.Column('auth_date_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='私有密码过期时间'),
    sa.Column('time_over', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='私有规则过期'),
    sa.Column('b64_value', mysql.TEXT(collation='utf8mb4_bin'), nullable=True, comment='64编码'),
    sa.Column('home_url', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='规则主页链接'),
    sa.Column('pic_url', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='网站图标链接'),
    sa.Column('is_json', mysql.TINYINT(display_width=1), server_default=sa.text('1'), autoincrement=False, nullable=True, comment='是否json值'),
    sa.Column('is_redirect', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否为后端重定向'),
    sa.Column('is_tap', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否为仓库跳转规则'),
    sa.Column('can_discuss', mysql.TINYINT(display_width=1), server_default=sa.text('1'), autoincrement=False, nullable=True, comment='是否可以互动'),
    sa.Column('is_json_list', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否json列表'),
    sa.Column('data_type', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("'home_rule_url'"), nullable=True, comment='数据类型'),
    sa.Column('version', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("'0'"), nullable=True, comment='版本号'),
    sa.Column('author', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=True, comment='作者'),
    sa.Column('note', mysql.TEXT(collation='utf8mb4_bin'), nullable=True, comment='说明'),
    sa.Column('good_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='点赞数'),
    sa.Column('bad_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='踩数'),
    sa.Column('reply_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='回复数'),
    sa.Column('is_safe', mysql.TINYINT(display_width=1), server_default=sa.text('1'), autoincrement=False, nullable=True, comment='是否安全'),
    sa.Column('is_good', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否优质'),
    sa.Column('is_white', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否白名单'),
    sa.Column('not_safe_note', mysql.TEXT(collation='utf8mb4_bin'), nullable=True, comment='风险描述'),
    sa.Column('last_active', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='开发者上次提交时间'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_hiker_rule_id', 't_hiker_rule', ['id'], unique=False)
    op.create_table('t_config_settings',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=64), server_default=sa.text("''"), nullable=False, comment='参数名称'),
    sa.Column('key', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=False, comment='参数键名'),
    sa.Column('value', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=False, comment='参数键值'),
    sa.Column('remark', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("''"), nullable=True, comment='备注'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态 0: 正常  1:停用'),
    sa.Column('order_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='排序'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_config_settings_name', 't_config_settings', ['name'], unique=False)
    op.create_index('ix_t_config_settings_id', 't_config_settings', ['id'], unique=False)
    op.create_table('t_user_role',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_user_role_id', 't_user_role', ['id'], unique=False)
    op.create_table('t_hiker_developer',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=False, comment='开发者账号'),
    sa.Column('qq', mysql.VARCHAR(collation='utf8mb4_bin', length=11), nullable=False, comment='QQ号'),
    sa.Column('password', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("'123456'"), nullable=False, comment='开发者密码'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态'),
    sa.Column('is_manager', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否超管'),
    sa.Column('active', mysql.TINYINT(display_width=1), server_default=sa.text('1'), autoincrement=False, nullable=True, comment='是否启用'),
    sa.Column('test', mysql.VARCHAR(collation='utf8mb4_bin', length=10), nullable=True, comment='测试字段'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_hiker_developer_id', 't_hiker_developer', ['id'], unique=False)
    op.create_table('t_menus',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('path', mysql.VARCHAR(collation='utf8mb4_bin', length=128), server_default=sa.text("''"), nullable=True, comment='路由'),
    sa.Column('component', mysql.VARCHAR(collation='utf8mb4_bin', length=128), server_default=sa.text("''"), nullable=True, comment='组件'),
    sa.Column('is_frame', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否外链'),
    sa.Column('hidden', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否隐藏'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='菜单状态'),
    sa.Column('order_num', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='显示排序'),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=32), server_default=sa.text("''"), nullable=True, comment='唯一标识用于页面缓存，否则keep-alive会出问题'),
    sa.Column('title', mysql.VARCHAR(collation='utf8mb4_bin', length=32), server_default=sa.text("''"), nullable=True, comment='标题'),
    sa.Column('icon', mysql.VARCHAR(collation='utf8mb4_bin', length=32), server_default=sa.text("''"), nullable=True, comment='图标'),
    sa.Column('no_cache', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否缓存'),
    sa.Column('parent_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='上级菜单'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_menus_id', 't_menus', ['id'], unique=False)
    op.create_table('t_users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('username', mysql.VARCHAR(collation='utf8mb4_bin', length=32), nullable=False, comment='用户名'),
    sa.Column('nickname', mysql.VARCHAR(collation='utf8mb4_bin', length=32), server_default=sa.text("''"), nullable=False, comment='姓名'),
    sa.Column('sex', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='性别'),
    sa.Column('phone', mysql.VARCHAR(collation='utf8mb4_bin', length=32), nullable=False, comment='手机号'),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_bin', length=256), nullable=False, comment='邮箱'),
    sa.Column('hashed_password', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=False, comment='密码'),
    sa.Column('avatar', mysql.VARCHAR(collation='utf8mb4_bin', length=128), server_default=sa.text("''"), nullable=True, comment='头像'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False, comment='状态'),
    sa.Column('is_active', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否已经验证用户'),
    sa.Column('is_superuser', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='是否超级管理员'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_users_username', 't_users', ['username'], unique=False)
    op.create_index('ix_t_users_id', 't_users', ['id'], unique=False)
    op.create_table('t_perm_label',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='创建时间'),
    sa.Column('creator_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='创建人id'),
    sa.Column('modified_time', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=True, comment='更新时间'),
    sa.Column('modifier_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='修改人id'),
    sa.Column('is_deleted', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('label', mysql.VARCHAR(collation='utf8mb4_bin', length=128), server_default=sa.text("''"), nullable=True, comment='标签'),
    sa.Column('remark', mysql.VARCHAR(collation='utf8mb4_bin', length=256), server_default=sa.text("''"), nullable=True, comment='备注'),
    sa.Column('status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_t_perm_label_id', 't_perm_label', ['id'], unique=False)
    # ### end Alembic commands ###
