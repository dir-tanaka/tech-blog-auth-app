"""create account table

Revision ID: daa2aa49f10d
Revises: 
Create Date: 2025-07-30 23:32:23.900552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'daa2aa49f10d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user',
        # id: 主キー、自動インクリメント
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        
        # email: 文字列、インデックス付き
        sa.Column('email', sa.String(), index=True),
        
        # password_hash: 文字列、インデックス付き
        sa.Column('password_hash', sa.String(), index=True),

        # password_hash: 文字列、インデックス付き
        sa.Column('salt', sa.String(), index=True),
        
        # created_at: タイムゾーン付き日時型
        # server_default: データベース側でデフォルト値を設定（DBの方言に合わせる必要があります）
        # Pythonのdefault/onupdate設定はDBに反映されないため、ここでは省略するかDBの方言に合わせます。
        # データベースに依存しない汎用的な定義
        sa.Column(
            'created_at', 
            sa.DateTime(timezone=True), 
            # データベースによってはサーバー側でのデフォルト値設定が必要な場合があります。
            # 例（PostgreSQLの場合）：server_default=sa.text('TIMEZONE(\'Asia/Tokyo\', NOW())') 
        ),
        
        # updated_at: タイムゾーン付き日時型
        sa.Column(
            'updated_at', 
            sa.DateTime(timezone=True),
            # データベースによってはサーバー側でのデフォルト値設定が必要な場合があります。
            # 例（PostgreSQLの場合）：server_default=sa.text('TIMEZONE(\'Asia/Tokyo\', NOW())')
        ),
    )
    
    # Alembicでは、Columnのindex=Trueはop.create_table内で定義するか、
    # op.create_indexで別途作成しますが、ここではop.create_table内に集約します。
    # id, email, password_hash のインデックスは primary_key=True や Column(..., index=True) で定義されているため、
    # created_at と updated_at のインデックスを追加で作成します。
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_updated_at'), 'user', ['updated_at'], unique=False)

def downgrade():
    op.drop_table('user')
